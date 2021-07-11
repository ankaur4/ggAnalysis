from CRABClient.UserUtilities import config #getUsernameFromSiteDB
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
#General
config.General.requestName = 'UL2017D_Data'# 'UL2016G_Data' # 'UL2016F_Data'
config.General.workArea = 'SMcrabrun16'
config.General.transferOutputs = True
config.General.transferLogs = True
#JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../run_data2017_106X.py' # on which did cmsRun
config.JobType.outputFiles = ['ntuple.root']
config.JobType.allowUndistributedCMSSW = True  #was getting error and this was in reccomendation
#Data
config.Data.inputDataset =' /SingleMuon/Run2017D-09Aug2019_UL2017-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.lumiMask = 'Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
config.Data.splitting = 'LumiBased' #in data analysis lumibased splitting is used
config.Data.unitsPerJob = 50  #on the basis of which splitting is based and will decide the run time of jobs,it will not effect the no. of events but splitting of jobs only
config.Data.publication = False
#output path
config.Data.outLFNDirBase = '/store/group/leptonjets/ankaur/Ntuples_UL17/SingleMuon'
config.Site.storageSite ='T3_US_FNALLPC'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
        print config.General.requestName
        crabCommand('submit', config = config)
                                                         
