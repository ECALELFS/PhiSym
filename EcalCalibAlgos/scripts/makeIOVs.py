#!/usr/bin/env python
# import ROOT in batch mode
import sys
import os
import json
import subprocess
from commands import getstatusoutput

oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
from optparse import OptionParser
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ librarie
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.gSystem.Load("libDataFormatsEcalDetId.so");
ROOT.gSystem.Load("libPhiSymEcalCalibDataFormats.so");
ROOT.AutoLibraryLoader.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events, Lumis

from FWCore.PythonUtilities.LumiList import LumiList

# Load TFile and TTree
from ROOT import TTree, TFile

# getting arrays
#from array import array
import numpy as n

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
#lumis = Lumis("file:/tmp/zwimpee/CMSSW_746-weights-74X_dataRun2_Prompt_v0-Run2015B_v3_test.root")

def resetInterval( interval , index ):
    interval["index"] = index
    interval["firstRun"] = 0
    interval["firstLumi"] = 0
    interval["unixTimeStart"] = 0
    interval["lastRun"] = 0
    interval["lastLumi"] = 0
    interval["unixTimeEnd"] = 0
    interval["norm"] = 0
    interval["nHit"] = 0
    interval["nLS"] =0
    interval["unixTimeMean"] = 0
    interval["flag"] = ""

def closeInterval( interval ):
    interval["unixTimeMean"]=interval["unixTimeStart"]+float(interval["unixTimeMean"])/float(interval["norm"])

def startInterval( interval, run, lumi, start ):
    interval["firstRun"] = run
    interval["firstLumi"] = lumi
    interval["unixTimeStart"] = start

parser = OptionParser()
parser.add_option("", "--debug", dest="debug", action='store_true')
parser.add_option("", "--saveIsolatedIntervals", dest="saveIsolatedIntervals", action='store_true')
parser.add_option("-n", "--maxHit", dest="maxHit", type="int", default=7000000000)
parser.add_option("-f", "--fileList", dest="fileList", type="string", default="fileList.txt")
parser.add_option("-d", "--dataset", dest="dataset", type="string", default="")
parser.add_option("-o", "--output", dest="output", type="string", default="readMap.root")
parser.add_option("-p", "--prefix", dest="prefix", type="string", default="root://xrootd-cms.infn.it/")
parser.add_option("-t","--maxTime", dest="maxTime", type = "int", default=86400)
parser.add_option("-j","--jsonFile", dest="jsonFile", type = "string", default="")
(options, args) = parser.parse_args()

if options.dataset != "":
    print "Getting files from DAS for dataset "+options.dataset
    if getstatusoutput("das_client.py --query='file dataset="+options.dataset+" instance=prod/phys03' --limit 0 | grep '/store/' > /tmp/filelist.dat"):
        options.fileList = "/tmp/filelist.dat"

with open(options.fileList,'r') as textfile:
    files = [line.strip() for line in textfile]

handlePhiSymInfo  = Handle ("std::vector<PhiSymInfo>")
labelPhiSymInfo = ("PhiSymProducer")

timeMap={}

### get PU informations
if options.jsonFile != "":
    lumiList = LumiList(os.path.expandvars(options.jsonFile))
    with open(options.jsonFile) as lumis_file:
        lumiJson = json.load(lumis_file)
        runs = lumiJson.keys()
else:
    cmd_lumi = subprocess.Popen(['${CMSSW_BASE}/src/PhiSym/EcalCalibAlgos/scripts/get_dataset_lumi_json.sh', options.dataset, 'phys03'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lumi_string, err_lumi = cmd_lumi.communicate()
    lumiJson = json.loads(lumi_string)
    runs = lumiJson.keys()
    
runs_string = ','.join(runs)

cmd_pu = subprocess.Popen(['${CMSSW_BASE}/src/PhiSym/EcalCalibAlgos/scripts/get_pu_info.sh '+runs_string+' > test.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
pu_string, err_pu = cmd_pu.communicate()
puJson = {}
with open('test.json') as pu_file:
    puJson = json.load(pu_file)
    
for aline in files:
    fullpath_file = options.prefix+aline
    if options.debug:
        print "Reading files:", options.prefix+aline

    try:
        lumis = Lumis(fullpath_file)
    except:
        print "File "+fullpath_file+" NOT FOUND!"
        continue;

    for i,lumi in enumerate(lumis):
        lumi.getByLabel(labelPhiSymInfo,handlePhiSymInfo)
        phiSymInfo = handlePhiSymInfo.product()
        # skipping BAD lumiSections
        if options.jsonFile != "" and not lumiList.contains(phiSymInfo.back().getStartLumi().run(),phiSymInfo.back().getStartLumi().luminosityBlock()):
            if options.debug:
                print "Lumi section not in json file"
            continue
        
        # normalization is rate * PU
        beginTime = lumi.luminosityBlockAuxiliary().beginTime().unixTime()
        run_num = str(lumi.luminosityBlockAuxiliary().run())
        lumi_num = str(lumi.luminosityBlockAuxiliary().luminosityBlock())
        if run_num not in puJson.keys() or lumi_num not in puJson[run_num].keys():
            print run_num
            print lumi_num
            #print puJson[run_num][lumi_num]
            print "Lumi skipped since not in puJson"
            continue
        timeMap[beginTime] = {
            "run" : phiSymInfo.back().getStartLumi().run(),
            "lumi" : phiSymInfo.back().getStartLumi().luminosityBlock(),
            #"totHitsEB" : phiSymInfo.back().GetTotHitsEB(),
            "norm" : phiSymInfo.back().GetNEvents()*float(puJson[run_num][lumi_num])
        }

        if options.debug:
            print "====>"
            print "Run "+str(phiSymInfo.back().getStartLumi().run())+" Lumi "+str(phiSymInfo.back().getStartLumi().luminosityBlock())+" beginTime "+str(beginTime)
            print "NEvents in this LS "+str(phiSymInfo.back().GetNEvents())
            print "TotHits EB "+str(phiSymInfo.back().GetTotHitsEB())+" Avg occ EB "+str(float(phiSymInfo.back().GetTotHitsEB())/phiSymInfo.back().GetNEvents()) 
            print "TotHits EE "+str(phiSymInfo.back().GetTotHitsEE())+" Avg occ EE "+str(float(phiSymInfo.back().GetTotHitsEE())/phiSymInfo.back().GetNEvents()) 
    
    # close current file
    lumis._tfile.Close()


nMaxHits=options.maxHit
maxStopTime=options.maxTime

interval={}

full_interval_count=0
isolated_interval_count=0

currentInterval={}
resetInterval( currentInterval , 0 )

# splitting logic
print("### Start splitting logic")
for key in sorted(timeMap):    
    if currentInterval["nLS"]==0 and currentInterval["unixTimeStart"]==0:
       #start a new interval
        startInterval( currentInterval, timeMap[key]["run"], timeMap[key]["lumi"], key)

    if key-currentInterval["unixTimeStart"]>=maxStopTime and currentInterval["unixTimeStart"] != 0:

        if currentInterval["norm"] >= nMaxHits/2.:
            # Enough statistics. Closing previous interval 
            if options.debug:
                print "Closing interval by time condition"

            closeInterval( currentInterval )
            currentInterval["flag"]="S"
            interval[ currentInterval["unixTimeStart" ] ]=dict(currentInterval)
            full_interval_count+=1

        else:
            lastInterval=-1
            if len(interval.keys())>0:
                lastInterval=sorted(interval.keys())[-1]
            if lastInterval>0:
                if (currentInterval["unixTimeEnd"]-interval[lastInterval]["unixTimeStart"]<=maxStopTime):
                #merging with last interval
                    if options.debug:
                        print "Merging interval"
                    closeInterval( currentInterval )
                    interval[lastInterval]["lastRun"]=currentInterval["lastRun"]
                    interval[lastInterval]["lastLumi"]=currentInterval["lastLumi"]
                    interval[lastInterval]["unixTimeEnd"]=currentInterval["unixTimeEnd"]
                    interval[lastInterval]["unixTimeMean"]=(interval[lastInterval]["unixTimeMean"]*interval[lastInterval]["norm"]+currentInterval["unixTimeMean"]*currentInterval["norm"])/(float(interval[lastInterval]["norm"]+currentInterval["norm"]))
                    interval[lastInterval]["nHit"]+=currentInterval["nHit"]
                    interval[lastInterval]["norm"]+=currentInterval["norm"]
                    interval[lastInterval]["flag"]="M"
                else:
                    if options.saveIsolatedIntervals:
                        if options.debug:
                            print "Save short interval"
                        closeInterval( currentInterval )
                        currentInterval["flag"]="I"
                        interval[ currentInterval["unixTimeStart" ] ]=dict(currentInterval)
                        full_interval_count+=1
                    else:
                        if options.debug:
                            print "Dropping interval"
                        #dropping interval
                        isolated_interval_count+=1
            else:
                if options.debug:
                    print "First interval is a short one!"
                if options.saveIsolatedIntervals:
                    if options.debug:
                        print "Save short interval"
                    closeInterval( currentInterval )
                    currentInterval["flag"]="I"
                    interval[ currentInterval["unixTimeStart" ] ]=dict(currentInterval)
                    full_interval_count+=1
                else:
                    if options.debug:
                        print "Dropping interval"
                    #dropping interval
                    isolated_interval_count+=1

        # Start a new interval
        resetInterval( currentInterval, full_interval_count )
        startInterval( currentInterval, timeMap[key]["run"], timeMap[key]["lumi"], key)

    currentInterval["lastRun"] = timeMap[key]["run"]
    currentInterval["lastLumi"] = timeMap[key]["lumi"]
    currentInterval["unixTimeEnd"] = key+23.1
    #currentInterval["nHit"] += timeMap[key]["totHitsEB"]
    currentInterval["norm"] += timeMap[key]["norm"]
    currentInterval["nLS"] +=1
    currentInterval["unixTimeMean"] += float((key-currentInterval["unixTimeStart"]+11.55)*timeMap[key]["norm"])
    
    if currentInterval["norm"] >= nMaxHits:
        # adding as new interval
        closeInterval( currentInterval )
        currentInterval["flag"]="F"
        interval[ currentInterval["unixTimeStart"] ]=dict(currentInterval)
        full_interval_count+=1
        # resetting for next interval
        resetInterval( currentInterval, full_interval_count )

interval_number=n.zeros(1,dtype=int)
hit=n.zeros(1,dtype=long)
norm=n.zeros(1,dtype=float)
flag=bytearray(2)
nLSBranch=n.zeros(1,dtype=int)
firstRunBranch=n.zeros(1,dtype=int)
lastRunBranch=n.zeros(1,dtype=int)
firstLumiBranch=n.zeros(1,dtype=int)
lastLumiBranch=n.zeros(1,dtype=int)
unixTimeStartBranch=n.zeros(1,dtype=float)
unixTimeEndBranch=n.zeros(1,dtype=float)
unixTimeMeanBranch=n.zeros(1,dtype=float)

outFile = ROOT.TFile(options.output, "RECREATE")
if not outFile:
    print "Cannot open outputFile "+options.output

tree = ROOT.TTree('iov_map', 'IOV map')
tree.Branch('index', interval_number, 'index/I')
tree.Branch('flag', flag, 'flag/C')
tree.Branch('nHit', hit, 'nHit/L')
tree.Branch('norm', norm, 'norm/D')
tree.Branch('nLS', nLSBranch, 'nLS/I')
tree.Branch('firstRun', firstRunBranch, 'firstRun/I')
tree.Branch('lastRun', lastRunBranch, 'lastRun/I')
tree.Branch('firstLumi', firstLumiBranch, 'firstLumi/I')
tree.Branch('lastLumi', lastLumiBranch, 'lastLumi/I')
tree.Branch('unixTimeStart', unixTimeStartBranch, 'unixTimeStart/D')
tree.Branch('unixTimeEnd', unixTimeEndBranch, 'unixTimeEnd/D')
tree.Branch('unixTimeMean', unixTimeMeanBranch, 'unixTimeMean/D')

for key in sorted(interval):
    interval_number[0]=interval[key]["index"]
    flag[0]=interval[key]["flag"][0]
    hit[0]=interval[key]["nHit"]
    norm[0]=interval[key]["norm"]
    nLSBranch[0]=interval[key]["nLS"]
    firstRunBranch[0]=interval[key]["firstRun"]
    lastRunBranch[0]=interval[key]["lastRun"]
    firstLumiBranch[0]=interval[key]["firstLumi"]
    lastLumiBranch[0]=interval[key]["lastLumi"]
    unixTimeStartBranch[0]=interval[key]["unixTimeStart"]
    unixTimeEndBranch[0]=interval[key]["unixTimeEnd"]
    unixTimeMeanBranch[0]=interval[key]["unixTimeMean"]
    tree.Fill()

outFile.Write()
outFile.Close()

if options.debug:
    for key in sorted(interval):
        print "------------------"
        print "Index: " + str(interval[key]["index"])
        print "nHit: " + str(interval[key]["nHit"])
        print "norm: " + str(interval[key]["norm"])
        print "nLS: " + str(interval[key]["nLS"])
        print "First Run: " + str(interval[key]["firstRun"])
        print "Last Run: " + str(interval[key]["lastRun"])
        print "First Lumi: " + str(interval[key]["firstLumi"])
        print "Last Lumi: " + str(interval[key]["lastLumi"])
        print "Unix Time Start: " + str(interval[key]["unixTimeStart"])
        print "Unix Time End: " + str(interval[key]["unixTimeEnd"])
        print "Unix Time Mean: " + str(interval[key]["unixTimeMean"])
        print "------------------"
                                  
print "====> FULL_INTERVALS:"+str(full_interval_count) + " ISOLATED INTERVALS:" + str(isolated_interval_count)

# erase tmp file
getstatusoutput("rm -fv /tmp/${USER}/filelist.dat")





