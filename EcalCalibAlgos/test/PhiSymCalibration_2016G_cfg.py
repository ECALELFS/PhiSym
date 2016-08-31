import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.IOVBounds = cms.PSet(
    startingIOV     = cms.int32(0),
    nIOVs           = cms.int32(-1),
    manualSplitting = cms.bool(False),
    beginRuns       = cms.vint32(),
    endRuns         = cms.vint32(),
    IOVMaps         = cms.vstring(
        "$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/ntuples/Run2016G_v1/IOVMap2016G.root"
    )
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    oldConstantsFiles = cms.vstring(''),
    
    recoConstantsFile = cms.string('/afs/cern.ch/work/s/spigazzi/ECAL/CMSSW_8_0_17/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2016B_prompt.dat'),
    
    inputFiles = cms.vstring([
        
        # RunG
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_1.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_10.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_11.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_12.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_13.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_14.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_15.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_16.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_17.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_18.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_19.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_2.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_20.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_21.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_22.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_23.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_24.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_25.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_26.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_27.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_28.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_29.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_3.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_30.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_31.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_32.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_33.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_34.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_35.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_36.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_37.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_38.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_39.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_4.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_40.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_41.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_42.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_43.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_44.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_45.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_46.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_47.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_48.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_49.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_5.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_50.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_51.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_52.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_53.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_54.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_55.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_56.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_57.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_58.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_59.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_6.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_60.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_61.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_62.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_63.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_64.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_65.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_66.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_67.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_68.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_69.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_7.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_70.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_71.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_72.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_73.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_74.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_75.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_76.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_77.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_78.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_79.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_8.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_80.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_81.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_82.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_83.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_84.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_85.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_86.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_87.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_88.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_89.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_9.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_90.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_91.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_92.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_93.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_94.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_95.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_96.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_97.root",
        "root://cms-xrd-transit.cern.ch//store/group/dpg_ecal/alca_ecalcalib/phiSymmetry/AlCaPhiSym/crab_PHISYM-CMSSW_8_0_17-weights-80X_dataRun2_Prompt_v10-Run2016G-merged_v1/160830_180657/0000/phisym_merged_98.root"

    ])
)

