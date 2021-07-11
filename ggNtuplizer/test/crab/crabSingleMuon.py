from CRABClient.UserUtilities import config #getUsernameFromSiteDB
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

config = config()
#General
config.General.requestName = 'UL2016F2_Data'# 'UL2016G_Data' # 'UL2016F_Data'
config.General.workArea = 'SMcrabrun16'
config.General.transferOutputs = True
config.General.transferLogs = True
#JobType
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skimMINIAOD_UL2017.py' # on which did cmsRun
config.JobType.outputFiles = ['tuple.root']
config.JobType.allowUndistributedCMSSW = True  #was getting error and this was in reccomendation
#Data
config.Data.inputDataset = '/SingleMuon/Run2016F-21Feb2020_UL2016_HIPM-v1/MINIAOD'#'/SingleMuon/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/MINIAOD' #'/SingleMuon/Run2016C-21Feb2020_UL2016-v1/MINIAOD' # '/SingleMuon/Run2016H-21Feb2020_UL2016-v1/MINIAOD'   #'/SingleMuon/Run2016G-21Feb2020_UL2016-v1/MINIAOD' # '/SingleMuon/Run2016F-21Feb2020_UL2016-v1/MINIAOD'  #FRom DAS
config.Data.inputDBS = 'global'
config.Data.lumiMask = 'json_DCSONLY.txt'  #i downloaded from lxplus and then copied here in present directory
config.Data.splitting = 'LumiBased' #in data analysis lumibased splitting is used
config.Data.unitsPerJob = 40  #on the basis of which splitting is based and will decide the run time of jobs,it will not effect the no. of events but splitting of jobs only
config.Data.publication = False
#output path
config.Data.outLFNDirBase = '/store/user/ankaur/jetmet/SingleMuon/UL2016F2/' #'/store/user/ankaur/jetmet/SingleMuon/UL2016H/'    #'/store/user/ankaur/jetmet/SingleMuon/UL2016G/' #'/store/user/ankaur/jetmet/SingleMuon/UL2016F/'
config.Site.storageSite ='T3_US_FNALLPC'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_')
        print config.General.requestName
        crabCommand('submit', config = config)
                                                         
