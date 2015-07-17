import FWCore.ParameterSet.Config as cms

process = cms.PSet()

nIOVs=1

process.IOVBounds = cms.PSet(
    startingIOV = cms.int32(16),
    nIOVs       = cms.int32(nIOVs),    
    # beginRuns   = cms.vint32(191043, 191086, 191247, 191691, 193093, 193336, 193834, 194051, 194150, 194223,
    #                          194429, 194480, 194691, 194912, 195147, 195396, 195633, 195913, 195963, 196249,
    #                          196452, 198202, 198268, 198941, 199011, 199356, 199698, 199804, 199960, 200152,
    #                          200473, 200990, 201159, 201278, 201657, 202012, 202084, 202237, 202478, 202504,
    #                          203830, 203909, 204113, 204563, 204564, 205086, 205111, 205233, 205312, 205339,
    #                          205666, 205774, 206088, 206243, 206389, 206466, 206539, 206744, 206897, 207214,
    #                          207269, 207454, 207897, 208297, 208390, 208538),
    beginRuns   = cms.vint32(251022, 251023, 251024, 251025, 251026, 251027, 251028,
                             251244, 251251, 251252, 251521, 251522, 251523, 251548,
                             251559, 251560, 251561, 251562),
    beginLumis  = cms.vint32(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                             -1, -1),
    # endRuns     = cms.vint32(191062, 191226, 191277, 191810, 193334, 193575, 194050, 194120, 194210,
    #                          194428, 194479, 194644, 194897, 195115, 195390, 195552, 195868, 195950,
    #                          196239, 196438, 196531, 198249, 198522, 199008, 199336, 199436, 199754,
    #                          199877, 200091, 200466, 200601, 201115, 201176, 201625, 201824, 202075,
    #                          202209, 202477, 202478, 202504, 203912, 204101, 204555, 204601, 205085,
    #                          205310, 205217, 205311, 205617, 205627, 205718, 206066, 206210, 206331,
    #                          206448, 206513, 206605, 206869, 207100, 207233, 207398, 207518, 207924,
    #                          208357, 208487, 208686),
    endRuns     = cms.vint32(251022, 251023, 251024, 251025, 251026, 251027, 251028,
                             251244, 251251, 251252, 251521, 251522, 251523, 251548,
                             251559, 251560, 251561, 251562),
    #endRuns     = cms.vint32(251244),
    endLumis    = cms.vint32(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
                             -1, -1)
)

process.ioFilesOpt = cms.PSet(    
    outputFile = cms.string('summed_'),
    
    #oldConstantsFiles = cms.vstring(),
    oldConstantsFiles = cms.vstring('$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012D_newThr.dat'),
    
    #recoConstantsFile = cms.string('/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_1/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2012DAbs.dat'),
    recoConstantsFile = cms.string('$CMSSW_BASE/src/PhiSym/EcalCalibAlgos/data/EcalIntercalibConstants_2015Abs.dat'),
    
    inputFiles = cms.vstring(
        [
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_1.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_10.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_100.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_101.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_102.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_103.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_104.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_105.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_106.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_107.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_108.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_109.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_11.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_110.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_111.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_112.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_113.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_114.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_115.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_116.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_117.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_118.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_119.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_12.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_120.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_121.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_122.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_123.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_124.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_125.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_126.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_127.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_128.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_129.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_13.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_130.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_131.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_132.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_133.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_134.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_135.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_136.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_137.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_138.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_139.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_14.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_140.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_141.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_142.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_143.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_144.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_145.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_146.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_147.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_148.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_149.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_15.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_150.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_151.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_152.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_153.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_154.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_155.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_156.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_157.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_158.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_159.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_16.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_160.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_161.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_162.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_163.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_164.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_165.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_166.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_167.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_168.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_169.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_17.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_170.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_171.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_172.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_173.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_174.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_175.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_176.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_177.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_178.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_179.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_18.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_180.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_181.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_182.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_183.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_184.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_185.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_186.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_187.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_188.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_189.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_19.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_190.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_191.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_192.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_193.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_194.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_195.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_196.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_2.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_20.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_21.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_22.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_23.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_24.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_25.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_26.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_27.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_28.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_29.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_3.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_30.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_31.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_32.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_33.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_34.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_35.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_36.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_37.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_38.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_39.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_4.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_40.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_41.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_42.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_43.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_44.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_45.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_46.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_47.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_48.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_49.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_5.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_50.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_51.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_52.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_53.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_54.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_55.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_56.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_57.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_58.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_59.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_6.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_60.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_61.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_62.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_63.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_64.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_65.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_66.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_67.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_68.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_69.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_7.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_70.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_71.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_72.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_73.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_74.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_75.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_76.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_77.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_78.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_79.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_8.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_80.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_81.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_82.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_83.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_84.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_85.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_86.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_87.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_88.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_89.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_9.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_90.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_91.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_92.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_93.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_94.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_95.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_96.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_97.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_98.root",
            "/afs/cern.ch/user/s/spigazzi/work/ECAL/CMSSW_7_4_6_patch6/src/PhiSym/EcalCalibAlgos/ntuples/2015B_newGT/phisym_intercalibs_1000blocks_99.root"
        ])
)

#for iov in range(0, nIOVs):
    #process.ioFilesOpt.oldConstantsFiles.append('/afs/cern.ch/cms/CAF/CMSALCA/ALCA_ECALCALIB/energy-calibration-repository/phiSymmetry/2012D_LTCorrJan13/EcalIntercalibConstants_Oct13Jump_Corr_2012D_'+str(process.IOVBounds.beginRuns[iov])+'_'+str(process.IOVBounds.endRuns[iov])+'_Absolute.txt')
    #process.ioFilesOpt.oldConstantsFiles.append('/afs/cern.ch/cms/CAF/CMSALCA/ALCA_ECALCALIB/energy-calibration-repository/phiSymmetry/2012D_NewLaserTag/EcalIntercalibConstants_NLT_2012D_'+str(process.IOVBounds.beginRuns[iov])+'_'+str(process.IOVBounds.endRuns[iov])+'_NewCodeChecked_Absolute.txt')

