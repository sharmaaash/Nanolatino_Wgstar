# Originally from DY but comared to ggH/Full2016/sample.py

import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

# samples

samples={}

################################################
################# SKIMS ########################
################################################

#DATaMetCor='__metXYshift_2016'
#DATaMetCor=''
skim=''
#skim='__wwSel'
#skim='__topSel'
#skim='__topSel'
#skim='__vh3lSel' 
#skim='__sfSel' 
#skim='__vbsSel'
#skim='__ssSel'

#if skim =='__vh3lSel' :  skimFake='__vh3lFakeSel'
#else:                    skimFake=skim

##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/' 
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
elif 'knu' in SITE :
  treeBaseDir = '/pnfs/knu.ac.kr/data/cms/store/user/salee/Full2016_Apr17/'
  copiedTreeBaseDir = '/pnfs/knu.ac.kr/data/cms/store/user/spak/LatinoTree/Full2016_Apr17/'
elif 'sdfarm' in SITE : # KISTI T3
  xrootdPath  = 'root://cms-xrdr.sdfarm.kr:1094/'
  treeBaseDir = '/xrootd/store/group/hww/Full2016_Apr17/'



directory = treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017/'


################################################
############ NUMBER OF LEPTONS #################
################################################

#Nlep='2'
Nlep='3'
#Nlep='4'

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'puWeight*TriggerEffWeight_3l*EMTFbug_veto*Lepton_RecoSF[0]*Lepton_RecoSF[1]*Lepton_RecoSF[2]'
#SFweight      = 'SFweight'+Nlep+'l'
GenLepMatch   = 'GenLepMatch'+Nlep+'l'

################################################
############### B-Tag  WP ######################
################################################

#bAlgo='cmvav2'
#bAlgo='csvv2ivf'
#bAlgo='DeepCSVB'

#SFweight += '*btagSF'

#bWP='L'
#bWP='M'
#bWP='T'

# ... bPog SF and b veto

#bSF='1.'
#bVeto='1'
#if   bAlgo == 'cmvav2' :
# bSF='bPogSF_CMVA'+bWP
# bVeto='bveto_CMVA'+bWP
#elif bAlgo == 'csvv2ivf' :
# bSF='bPogSF_CSV'+bWP
# bVeto='bveto_CSV'+bWP
#elif bAlgo == 'DeepCSVB' :
# bSF='bPogSF_deepCSV'+bWP
# bVeto='bveto_deepCSV'+bWP

#SFweight += '*'+bSF
# Fix for 2-leptons for which this was kept in global formula !
#if Nlep == '2' : SFweight += '/bPogSF_CMVAL'


################################################
############### Lepton WP ######################
################################################

#... Electron:

eleWP='mvaFall17Iso_WP90'
#eleWP='cut_WP_Tight80X_SS'
#eleWP='mva_80p_Iso2015'
#eleWP='mva_80p_Iso2016'
#eleWP='mva_90p_Iso2015'
#eleWP='mva_90p_Iso2016'

#... Muon:

muWP='cut_Tight_HWWW'
#... Build formula

LepWPCut        = '1'
#LepWPweight     = 'LepSF2l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
#LepWPweight     = '1'

#SFweight += '*'+LepWPweight+'*'+LepWPCut

#... And the fakeW

#if Nlep == '2' :
#  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
#else:
#  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'

if Nlep == '2' or Nlep == '3' :
  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-31Mar2018-v1'] ,
                                                ['C','Run2017C-31Mar2018-v1'] ,
                                                ['D','Run2017D-31Mar2018-v1'] ,
                                                ['E','Run2017E-31Mar2018-v1'] ,
                                                ['F','Run2017F-31Mar2018-v1']

          ]


DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }

###########################################
#############  BACKGROUNDS  ###############
###########################################


###### DY #######

#useDYHT = False       # be carefull DY HT is LO 
useDYtt = True    
#mixDYttandHT = False  # be carefull DY HT is LO (HT better stat for HT>450 GEV)

### These weights were evaluated on ICHEP16 MC -> Update ?
ptllDYW_NLO = '1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-12.5151)/5.51582))'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50', True,'nanoLatino_')     
                                  + getSampleFiles(directory,'DYJetsToLL_M-50-LO-ext1', True,'nanoLatino_')     ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 1 ,
                 }

cutSF = '(abs(Lepton_pdgId[0]*Lepton_pdgId[1]) == 11*11)||(abs(Lepton_pdgId[0]*Lepton_pdgId[1]) == 13*13)'

addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO',ptllDYW_NLO)

if useDYtt :

  samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToTT_MuEle_M-50',True,'nanoLatino_')
                                  + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',True,'nanoLatino_'),
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                       'FilesPerJob' : 5 ,
                       }

  addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
  addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

else:

  samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50',True,'nanoLatino_')
                                  + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',True,'nanoLatino_'),
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                       'FilesPerJob' : 5 ,
                       }

  addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
  addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

samples['top'] = {    'name'   :   getSampleFiles(directory,'TTTo2L2Nu',True,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_tW_antitop',True,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_tW_top',True,'nanoLatino_')
                                 + getSampleFiles(directory,'ST_s-channel',True,'nanoLatino_') 
                                 + getSampleFiles(directory,'ST_t-channel_antitop',True,'nanoLatino_') 
                                 + getSampleFiles(directory,'ST_t-channel_top',True,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 2 ,
}

############ WW ############
samples['WW'] = {    'name'   :   getSampleFiles(directory,'WWTo2L2Nu',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToENEN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToMNMN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToENMN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToMNEN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToTNEN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToENTN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToMNTN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToTNMN',True,'nanoLatino_')
                                + getSampleFiles(directory,'GluGluToWWToTNTN',True,'nanoLatino_'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*nllW' ,
                     'FilesPerJob' : 4 ,                    
                     }

samples['WWewk'] = {   'name'  : getSampleFiles(directory, 'WpWmJJ_EWK',True,'nanoLatino_'),
                       'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*(Sum$(abs(GenPart_pdgId)==6)==0)' #filter tops
}

samples['Vg'] = {    'name'   : getSampleFiles(directory,'Wg_MADGRAPHMLM',True,'nanoLatino_') 
                              + getSampleFiles(directory,'Zg',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(!(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 ))',
                      'FilesPerJob' : 20 ,
}

samples['VZ'] = {    'name'   : getSampleFiles(directory,'ZZTo2L2Nu',True,'nanoLatino_')
                     + getSampleFiles(directory,'WZTo2L2Q',True,'nanoLatino_')
                     + getSampleFiles(directory,'ZZTo2L2Q',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*1.11' ,
                     'FilesPerJob' : 20 ,
}

samples['VVV'] = {    'name'   : getSampleFiles(directory,'WWW',True,'nanoLatino_') 
                      + getSampleFiles(directory,'WWZ',True,'nanoLatino_') 
                      + getSampleFiles(directory,'WZZ',True,'nanoLatino_') 
                      + getSampleFiles(directory,'ZZZ',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                      'FilesPerJob' : 5 ,
}

samples['ggWW']  = {  'name'   :   getSampleFiles(directory,'GluGluToWWToENEN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToENMN',True,'nanoLatino_') 
                                 + getSampleFiles(directory,'GluGluToWWToENTN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToMNEN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToMNMN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToMNTN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToTNEN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToTNMN',True,'nanoLatino_')
                                 + getSampleFiles(directory,'GluGluToWWToTNTN',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC , 
}

samples['WZgS']  = {  'name'   :   getSampleFiles(directory,'WZTo3LNu',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'* (Gen_ZGstar_mass >0 && Gen_ZGstar_mass > 4)' ,
}

###########################################
#############   SIGNALS  ##################
###########################################

############ ggH H->WW ############
samples['ggH_hww']  = {  'name'   :   getSampleFiles(directory,'GluGluHToWWTo2L2NuPowheg_M125',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     }
############ ZH H->WW ############
samples['ZH_hww']  = {  'name'   :   getSampleFiles(directory,'HZJ_HToWW_M120',True,'nanoLatino_'), #FIXME replace with 125 GeV sample when available
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
}

############ WH H->WW ############
samples['WH_hww']  = {  'name'   :   getSampleFiles(directory,'HWplusJ_HToWW_M125',True,'nanoLatino_')
                                   + getSampleFiles(directory,'HWminusJ_HToWW_M125',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
}

############ ttH ############
samples['H_htt'] = {  'name'   :   getSampleFiles(directory,'GluGluHToTauTau_M125',True,'nanoLatino_')
                                 + getSampleFiles(directory,'VBFHToTauTau_M125',True,'nanoLatino_')
                                 + getSampleFiles(directory,'HZJ_HToTauTau_M125',True,'nanoLatino_')
                                 + getSampleFiles(directory,'HWplusJ_HToTauTau_M125',True,'nanoLatino_')
                                 + getSampleFiles(directory,'HWminusJ_HToTauTau_M125',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
}

############ VBF H->WW ############
samples['qqH_hww']  = {  'name'   :   getSampleFiles(directory,'VBFHToWWTo2L2NuPowheg_M125_PrivateNano',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
}

samples['ggZH_hww']  = {  'name'   :   getSampleFiles(directory,'GluGluZH_HToWW_M125',True,'nanoLatino_'),
                        'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
}

############ VgS ############

#FIXME Add normalization k-factor
samples['VgS']  =  {  'name'   :   getSampleFiles(directory,'Wg_MADGRAPHMLM',True,'nanoLatino_')
                                 + getSampleFiles(directory,'Zg',True,'nanoLatino_')
                                 + getSampleFiles(directory,'WZTo3LNu_mllmin01',True,'nanoLatino_'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
                      'FilesPerJob' : 5 ,
                   }
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass >0)')
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass>=0.1 || Gen_ZGstar_mass<0)')

############ ttH ############

samples['ttH_hww']  = {  'name'   :   getSampleFiles(directory,'ttHToNonbb_M125',True,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     }


###########################################
################## FAKE ###################
###########################################

samples['Fake']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+fakeW,              #   weight/cut
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 20 ,
}
    
                    
                    
               
                   

for Run in DataRun :
  directory = treeBaseDir+'Run2017_nAOD_v1_Full2017v2/DATAl1loose2017v2__DATACorr2017__l2loose__fakeWp2NB/'
  for DataSet in DataSets :
   FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
   for iFile in FileTarget:
      samples['Fake']['name'].append(iFile)
      samples['Fake']['weights'].append(DataTrig[DataSet])

###########################################
################## DATA ###################
###########################################

samples['DATA']  = {   'name': [ ] ,     
                       'weight' : 'EMTFbug_veto'+'*'+METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],                            
                       'FilesPerJob' : 4 ,
                  }

for Run in DataRun :
#  if DATaMetCor is not '':
    directory = treeBaseDir+'Run2017_nAOD_v1_Full2017v2/DATAl1loose2017v2__DATACorr2017__l2loose__l2tightOR2017/'
#  else:
#    directory = treeBaseDir+'Apr2017_Run2016'+Run[0]+'_RemAOD/WgStarsel__hadd__EpTCorr__TrigMakerData__cleanTauData__formulasDATA/'
    for DataSet in DataSets :
     FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
     for iFile in FileTarget:
       print(iFile)
       samples['DATA']['name'].append(iFile)
       samples['DATA']['weights'].append(DataTrig[DataSet]) 

