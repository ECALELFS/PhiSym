import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.IOVBounds = cms.PSet(
    startingIOV     = cms.int32(0),
    nIOVs           = cms.int32(-1),
    manualSplitting = cms.bool(False),
    beginRuns       = cms.vint32(),
    endRuns         = cms.vint32(),
    IOVMaps         = cms.vstring(
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v1/IOVmap.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/IOVmap.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/IOVmap2016B_1D.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/IOVmap2016B.root"
    )
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring(''),
    
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_7/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2016B_prompt.dat'),
    
    inputFiles = cms.vstring([
        # # 2016B_v2 weights
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_11.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_12.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_13.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_14.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_15.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_16.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_17.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_18.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_19.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_1.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_20.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_21.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_22.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_23.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_24.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_25.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_26.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_27.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_28.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_29.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_2.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_30.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_31.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_32.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_33.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_34.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_35.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_36.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_37.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_38.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_39.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_3.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_40.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_41.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_42.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_43.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_44.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_45.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_46.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_47.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_48.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_49.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_4.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_50.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_51.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_52.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_53.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_54.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_55.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_56.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_57.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_5.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v2/phisym_merged_9.root"

        # # v3 with correct EE thresholds
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_1.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_11.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_12.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_13.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_14.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_15.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_16.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_17.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_18.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_19.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_20.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_21.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_22.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_23.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_24.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_25.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_26.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_27.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_28.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_3.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_30.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_31.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_32.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_33.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_34.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_35.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_36.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_37.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_38.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_39.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_4.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_40.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_41.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_42.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_43.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_44.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_45.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_48.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_49.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_5.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_50.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_51.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_53.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_54.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_55.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_56.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_57.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_6.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_7.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_8.root",
        # "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v3/phisym_merged_9.root"

        # v4 with correct EE thresholds
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_10.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_101.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_102.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_103.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_104.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_105.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_106.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_107.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_108.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_109.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_11.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_110.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_111.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_113.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_114.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_115.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_116.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_117.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_12.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_120.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_121.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_123.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_124.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_126.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_127.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_128.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_129.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_13.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_130.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_131.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_133.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_134.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_135.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_136.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_137.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_138.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_139.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_14.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_140.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_141.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_142.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_143.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_145.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_146.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_147.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_148.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_149.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_15.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_150.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_16.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_17.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_18.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_19.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_2.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_20.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_22.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_23.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_24.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_25.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_26.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_27.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_28.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_29.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_3.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_30.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_31.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_32.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_33.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_34.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_35.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_36.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_37.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_38.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_39.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_4.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_41.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_43.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_44.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_45.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_46.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_47.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_48.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_49.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_5.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_50.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_52.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_53.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_54.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_55.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_56.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_58.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_6.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_60.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_61.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_62.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_64.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_65.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_66.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_67.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_68.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_69.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_7.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_70.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_71.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_72.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_73.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_74.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_75.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_76.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_77.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_78.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_79.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_8.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_80.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_81.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_82.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_83.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_84.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_85.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_86.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_87.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_88.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_89.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_9.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_90.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_91.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_92.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_93.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_94.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_95.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_96.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_97.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_98.root",
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/2016B_v4/phisym_merged_99.root"
        
    ])
)

