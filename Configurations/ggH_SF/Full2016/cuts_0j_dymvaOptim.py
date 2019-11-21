
supercut = ' mll > 12 \
             && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[2]<10 \
             && (abs(std_vector_lepton_flavour[1]) == 13 || (std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>13) )  \
             && metTtrk > 20 && dymvaggh > 0.6 \
           '

optim={}
optim['dymva0p80']  = ' && dymvaggh > 0.80 ' 
optim['dymva0p85']  = ' && dymvaggh > 0.85 ' 
optim['dymva0p90']  = ' && dymvaggh > 0.90 ' 
optim['dymva0p91']  = ' && dymvaggh > 0.91 ' 
optim['dymva0p92']  = ' && dymvaggh > 0.92 ' 
optim['dymva0p93']  = ' && dymvaggh > 0.93 ' 
optim['dymva0p94']  = ' && dymvaggh > 0.94 ' 
optim['dymva0p945'] = ' && dymvaggh > 0.945 ' 
optim['dymva0p95']  = ' && dymvaggh > 0.95 ' 
optim['dymva0p955'] = ' && dymvaggh > 0.955 ' 
optim['dymva0p96']  = ' && dymvaggh > 0.96 ' 
optim['dymva0p965'] = ' && dymvaggh > 0.965 ' 
optim['dymva0p97']  = ' && dymvaggh > 0.97 ' 
optim['dymva0p975'] = ' && dymvaggh > 0.975 ' 
optim['dymva0p98']  = ' && dymvaggh > 0.98 ' 
optim['dymva0p99']  = ' && dymvaggh > 0.99 ' 
optim['dymva0p99']  = ' && dymvaggh > 0.995 ' 


for iCut in optim:
  
  # Higgs Signal Regions: ee/uu * 0/1 jet
  
  cuts['hww2l2v_13TeV_0jee_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
               && fabs(91.1876 - mll) > 15  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
               && std_vector_lepton_pt[0] < 53 \
               && std_vector_lepton_pt[1] < 34 \
               && mll < 60 \
                 ' + optim[iCut]
  
  cuts['hww2l2v_13TeV_0jmm_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
               && fabs(91.1876 - mll) > 15  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
               && std_vector_lepton_pt[0] < 53 \
               && std_vector_lepton_pt[1] < 34 \
               && mll < 60 \
                 ' + optim[iCut]
  
  ## Top CR: No H sel , bTag , tight DYmva
  
  cuts['hww2l2v_13TeV_top_0jee_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
               && fabs(91.1876 - mll) > 15  \
               && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                   || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                   || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                   || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                   || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                   || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                   || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                   || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                   || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                   || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                   ) \
                 ' + optim[iCut]
  
  cuts['hww2l2v_13TeV_top_0jmm_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
               && fabs(91.1876 - mll) > 15  \
               && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                   || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                   || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                   || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                   || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                   || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                   || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                   || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                   || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                   || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                   ) \
                 ' + optim[iCut]
  
  ## WW CR: No H Sel , mll>80, tight DYMva
  
  cuts['hww2l2v_13TeV_WW_0jee_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)  \
               && fabs(91.1876 - mll) > 15  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
               && mll > 80 \
                 ' + optim[iCut]
  
  cuts['hww2l2v_13TeV_WW_0jmm_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13) \
               && fabs(91.1876 - mll) > 15  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
               && mll > 80 \
                 ' + optim[iCut]
  
  ## DY Background IN with DYMVA>0.9X : Split ee/mm , No H cut !
  
  cuts['hww2l2v_13TeV_DYin_0jee_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
               && fabs(91.1876 - mll) < 7.5  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                 ' + optim[iCut]
   
  cuts['hww2l2v_13TeV_DYin_0jmm_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
               && fabs(91.1876 - mll) < 7.5  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                 ' + optim[iCut]
  
  cuts['hww2l2v_13TeV_DYin_0jdf_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
               && fabs(91.1876 - mll) < 7.5  \
               && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
               && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
               && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
               && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
               && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
               && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
               && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
               && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
               && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
               && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
                 ' + optim[iCut]
  
  ## DY Background IN with btag : Split ee/mm , No H cut !
  #  0jet only: Negligible DY background in 1jet bTag region
  
  cuts['hww2l2v_13TeV_DYin_btag_0jee_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
               && fabs(91.1876 - mll) < 7.5  \
               && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                   || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                   || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                   || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                   || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                   || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                   || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                   || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                   || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                   || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                   ) \
                 ' + optim[iCut]
  
  cuts['hww2l2v_13TeV_DYin_btag_0jmm_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
               && fabs(91.1876 - mll) < 7.5  \
               && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                   || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                   || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                   || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                   || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                   || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                   || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                   || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                   || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                   || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                   ) \
                 ' + optim[iCut]
  
  cuts['hww2l2v_13TeV_DYin_btag_0jdf_'+iCut] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
               && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
               && fabs(91.1876 - mll) < 7.5  \
               && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.5884 ) \
                   || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.5884 ) \
                   || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.5884 ) \
                   || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.5884 ) \
                   || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.5884 ) \
                   || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.5884 ) \
                   || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.5884 ) \
                   || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.5884 ) \
                   || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.5884 ) \
                   || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.5884 ) \
                   ) \
               ' + optim[iCut]


## Loose dymva + H sel for DY Acc
cuts['hww2l2v_13TeV_0jee_HAccNum'] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
             && std_vector_lepton_pt[0] < 53 \
             && std_vector_lepton_pt[1] < 34 \
             && mll < 60 \
             && dymvaggh > 0.6 \
               '

cuts['hww2l2v_13TeV_0jmm_HAccNum'] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
             && std_vector_lepton_pt[0] < 53 \
             && std_vector_lepton_pt[1] < 34 \
             && mll < 60 \
             && dymvaggh > 0.6 \
               '

## DY CR for Acc Denominator

cuts['hww2l2v_13TeV_0jee_AccDen'] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
             && dymvaggh > 0.6 \
               '

cuts['hww2l2v_13TeV_0jmm_AccDen'] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
             && fabs(91.1876 - mll) > 15  \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
             && dymvaggh > 0.6 \
               '

## Loose dymva + WW sel for DY Acc

cuts['hww2l2v_13TeV_WW_0jee_WWAccNum'] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)  \
             && fabs(91.1876 - mll) > 15  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
             && mll > 80 \
             && dymvaggh > 0.6  \
               '

cuts['hww2l2v_13TeV_WW_0jmm_WWAccNum'] = '( std_vector_jet_pt[0] < 30 && std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13) \
             && fabs(91.1876 - mll) > 15  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.5884 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.5884 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.5884 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.5884 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.5884 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.5884 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.5884 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.5884 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.5884 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.5884 ) \
             && mll > 80 \
             && dymvaggh > 0.6  \
               '
