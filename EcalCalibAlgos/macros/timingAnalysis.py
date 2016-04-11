# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
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

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
#lumis = Lumis("file:phisym.root")
#lumis = Lumis("root://xrootd-cms.infn.it//store/user/spigazzi/AlCaPhiSym/crab_PHISYM-CMSSW_741-weights-GR_P_V56-Run2015B_v1/150714_150558/0000/phisym_weights_1lumis_13.root")
lumis = Lumis("file:phisym_weights_1lumis_withtime_numEvent500000.root")

handlePhiSymInfo  = Handle ("std::vector<PhiSymInfo>")
handlePhiSymRecHitsEB  = Handle ("std::vector<PhiSymRecHit>")
handlePhiSymRecHitsEE  = Handle ("std::vector<PhiSymRecHit>")
labelPhiSymInfo = ("PhiSymProducer")
labelPhiSymRecHitsEB = ("PhiSymProducer","EB")
labelPhiSymRecHitsEE = ("PhiSymProducer","EE")

histos={}

histos["EB_TimeMean"]=ROOT.TH2F("EB_TimeMean","EB_TimeMean",360,0.5,360.5,171,-85.5,85.5)
histos["EB_TimeSum"]=ROOT.TH2F("EB_TimeSum","EB_TimeSum",360,0.5,360.5,171,-85.5,85.5)
histos["EB_TimeN"]=ROOT.TH2F("EB_TimeN","EB_TimeN",360,0.5,360.5,171,-85.5,85.5)

histos["EEM_TimeMean"]=ROOT.TH2F("EEM_TimeMean","EEM_TimeMean",100,0.5,100.5,100,0.5,100.5)
histos["EEM_TimeSum"]=ROOT.TH2F("EEM_TimeSum","EEM_TimeSum",100,0.5,100.5,100,0.5,100.5)
histos["EEM_TimeN"]=ROOT.TH2F("EEM_TimeN","EEM_TimeN",100,0.5,100.5,100,0.5,100.5)

histos["EEP_TimeMean"]=ROOT.TH2F("EEP_TimeMean","EEP_TimeMean",100,0.5,100.5,100,0.5,100.5)
histos["EEP_TimeSum"]=ROOT.TH2F("EEP_TimeSum","EEP_TimeSum",100,0.5,100.5,100,0.5,100.5)
histos["EEP_TimeN"]=ROOT.TH2F("EEP_TimeN","EEP_TimeN",100,0.5,100.5,100,0.5,100.5)

for i,lumi in enumerate(lumis):
    print "====>"
    lumi.getByLabel (labelPhiSymInfo,handlePhiSymInfo)
    lumi.getByLabel (labelPhiSymRecHitsEB,handlePhiSymRecHitsEB)
    lumi.getByLabel (labelPhiSymRecHitsEE,handlePhiSymRecHitsEE)
    phiSymInfo = handlePhiSymInfo.product()
    phiSymRecHitsEB = handlePhiSymRecHitsEB.product()
    phiSymRecHitsEE = handlePhiSymRecHitsEE.product()
    print "Run "+str(phiSymInfo.back().getStartLumi().run())+" Lumi "+str(phiSymInfo.back().getStartLumi().luminosityBlock())
    print "NEvents in this LS "+str(phiSymInfo.back().GetNEvents())
    print "TotHits EB "+str(phiSymInfo.back().GetTotHitsEB())+" Avg occ EB "+str(float(phiSymInfo.back().GetTotHitsEB())/phiSymInfo.back().GetNEvents()) 
    print "TotHits EE "+str(phiSymInfo.back().GetTotHitsEE())+" Avg occ EE "+str(float(phiSymInfo.back().GetTotHitsEE())/phiSymInfo.back().GetNEvents()) 

    print "EB PhiSymRecHits "+str(phiSymRecHitsEB.size())
    print "EE PhiSymRecHits "+str(phiSymRecHitsEE.size())

    for hit in phiSymRecHitsEB:
        myId=ROOT.EBDetId(hit.GetRawId())
        histos["EB_TimeSum"].Fill(myId.iphi(),myId.ieta(),hit.GetTimeSum())
        histos["EB_TimeN"].Fill(myId.iphi(),myId.ieta(),hit.GetTimeN())
    for hit in phiSymRecHitsEE:
        myId=ROOT.EEDetId(hit.GetRawId())
        if (myId.zside()<0):
            histos["EEM_TimeSum"].Fill(myId.ix(),myId.iy(),hit.GetTimeSum())
            histos["EEM_TimeN"].Fill(myId.ix(),myId.iy(),hit.GetTimeN())
        else:
            histos["EEP_TimeSum"].Fill(myId.ix(),myId.iy(),hit.GetTimeSum())
            histos["EEP_TimeN"].Fill(myId.ix(),myId.iy(),hit.GetTimeN())

for iPhi in range(1, 361):
    for iEta in range(1, 172):
        iBin = histos["EB_TimeN"].GetBin(iPhi, iEta)
        nTimeHits = histos["EB_TimeN"].GetBinContent(iBin)
        if nTimeHits > 0:
            histos["EB_TimeMean"].SetBinContent(iPhi, iEta, histos["EB_TimeSum"].GetBinContent(iBin)/nTimeHits)

for ix in range(1, 101):
    for iy in range(1, 101):
        iBin = histos["EEP_TimeN"].GetBin(ix, iy)
        nTimeHits = histos["EEP_TimeN"].GetBinContent(iBin)
        if nTimeHits > 0:
            histos["EEP_TimeMean"].SetBinContent(ix, iy, histos["EEP_TimeSum"].GetBinContent(iBin)/nTimeHits)

        iBin = histos["EEM_TimeN"].GetBin(ix, iy)
        nTimeHits = histos["EEM_TimeN"].GetBinContent(iBin)
        if nTimeHits > 0:
            histos["EEM_TimeMean"].SetBinContent(ix, iy, histos["EEM_TimeSum"].GetBinContent(iBin)/nTimeHits)
            
outFile=ROOT.TFile("phiSymTimeAnalysis.root","RECREATE")
for histo in histos.keys():
    histos[histo].Write()
outFile.Write()
outFile.Close()

