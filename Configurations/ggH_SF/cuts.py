
supercut = ' mll > 12 \
             && std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[2]<10 \
             && (abs(std_vector_lepton_flavour[1]) == 13 || std_vector_lepton_pt[1]>13)  \
             && metTtrk > 20 \
           '

#cuts['hww2l2v_13TeV_0jsf'] = 'std_vector_jet_pt[0] < 30 \
#             && ((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
#             || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)) \
#             && fabs(91.1876 - mll) > 15  \
#             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#             && std_vector_lepton_pt[0] < 52 \
#             && std_vector_lepton_pt[1] < 30 \
#             && mll < 60 \
#             && dymvaggh > 0.9607 \
#               '               

cuts['hww2l2v_13TeV_0jee'] = 'std_vector_jet_pt[0] < 30 \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && fabs(91.1876 - mll) > 15  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && std_vector_lepton_pt[0] < 52 \
             && std_vector_lepton_pt[1] < 30 \
             && mll < 60 \
             && dymvaggh > 0.9607 \
               '
               
cuts['hww2l2v_13TeV_1jee'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && fabs(91.1876 - mll) > 15  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && std_vector_lepton_pt[0] < 52 \
             && std_vector_lepton_pt[1] < 40 \
             && mll < 50 \
             && dymvaggh > 0.95 \
               '

#cuts['hww2l2v_13TeV_1jsf'] = '( std_vector_jet_pt[0] >= 30 ) \
#             && ( std_vector_jet_pt[1] < 30 ) \
#             && ((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
#             ||  (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11))  \
#             && fabs(91.1876 - mll) > 15  \
#             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#             && std_vector_lepton_pt[0] < 52 \
#             && std_vector_lepton_pt[1] < 40 \
#             && mll < 50 \
#             && dymvaggh > 0.95 \
#                '

cuts['hww2l2v_13TeV_0jmm'] = 'std_vector_jet_pt[0] < 30 \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && fabs(91.1876 - mll) > 15  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && std_vector_lepton_pt[0] < 52 \
             && std_vector_lepton_pt[1] < 30 \
             && mll < 60 \
             && dymvaggh > 0.9607 \
               '

cuts['hww2l2v_13TeV_1jmm'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && fabs(91.1876 - mll) > 15  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && std_vector_lepton_pt[0] < 52 \
             && std_vector_lepton_pt[1] < 40 \
             && mll < 50 \
             && dymvaggh > 0.95 \
               '


## Top CR: No H sel , bTag
#
#cuts['hww2l2v_13TeV_top_0jsf'] = 'std_vector_jet_pt[0] < 30 \
#             && ((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
#             || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)) \
#             && fabs(91.1876 - mll) > 15  \
#             && (   ( std_vector_jet_pt[0] > 20 && std_vector_jet_cmvav2[0] > -0.715 ) \
#                 || ( std_vector_jet_pt[1] > 20 && std_vector_jet_cmvav2[1] > -0.715 ) \
#                 || ( std_vector_jet_pt[2] > 20 && std_vector_jet_cmvav2[2] > -0.715 ) \
#                 || ( std_vector_jet_pt[3] > 20 && std_vector_jet_cmvav2[3] > -0.715 ) \
#                 || ( std_vector_jet_pt[4] > 20 && std_vector_jet_cmvav2[4] > -0.715 ) \
#                 || ( std_vector_jet_pt[5] > 20 && std_vector_jet_cmvav2[5] > -0.715 ) \
#                 || ( std_vector_jet_pt[6] > 20 && std_vector_jet_cmvav2[6] > -0.715 ) \
#                 || ( std_vector_jet_pt[7] > 20 && std_vector_jet_cmvav2[7] > -0.715 ) \
#                 || ( std_vector_jet_pt[8] > 20 && std_vector_jet_cmvav2[8] > -0.715 ) \
#                 || ( std_vector_jet_pt[9] > 20 && std_vector_jet_cmvav2[9] > -0.715 ) \
#                 ) \
#             && dymvaggh > 0.96 \
#               '
#
#cuts['hww2l2v_13TeV_top_1jsf'] = '( std_vector_jet_pt[0] >= 30 ) \
#             && ( std_vector_jet_pt[1] < 30 ) \
#             && ((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
#             || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)) \
#             && fabs(91.1876 - mll) > 15  \
#             && std_vector_jet_cmvav2[0]>-0.715 \
#             && dymvaggh > 0.95 \
#               '
#
## WW CR: No H Sel , mll>80
#
#cuts['hww2l2v_13TeV_WW_0jsf'] = 'std_vector_jet_pt[0] < 30 \
#             && ((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
#             || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)) \
#             && fabs(91.1876 - mll) > 15  \
#             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#             && mll > 80 \
#             && dymvaggh > 0.96 \
#               '
# 
#cuts['hww2l2v_13TeV_WW_1jsf'] = '( std_vector_jet_pt[0] >= 30 ) \
#             && ( std_vector_jet_pt[1] < 30 ) \
#             && ((std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
#             || (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)) \
#             && fabs(91.1876 - mll) > 15  \
#             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
#             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
#             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
#             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
#             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
#             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
#             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
#             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
#             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
#             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
#             && mll > 80 \
#             && dymvaggh > 0.95 \
#               '
#
## DY Background IN with DYMVA>0.9X : Split ee/mm , No H cut !
#
cuts['hww2l2v_13TeV_DYin_0jee'] = 'std_vector_jet_pt[0] < 30 \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && fabs(91.1876 - mll) < 7.5  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && dymvaggh > 0.96 \
               '
 
cuts['hww2l2v_13TeV_DYin_1jee'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*11)   \
             && fabs(91.1876 - mll) < 7.5 \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && dymvaggh > 0.95 \
               '

cuts['hww2l2v_13TeV_DYin_0jmm'] = 'std_vector_jet_pt[0] < 30 \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && fabs(91.1876 - mll) < 7.5  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && dymvaggh > 0.96 \
               '
 
cuts['hww2l2v_13TeV_DYin_1jmm'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -13*13)   \
             && fabs(91.1876 - mll) < 7.5 \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && dymvaggh > 0.95 \
               '

cuts['hww2l2v_13TeV_DYin_0jdf'] = 'std_vector_jet_pt[0] < 30 \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && fabs(91.1876 - mll) < 7.5  \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && dymvaggh > 0.96 \
               '
 
cuts['hww2l2v_13TeV_DYin_1jdf'] = '( std_vector_jet_pt[0] >= 30 ) \
             && ( std_vector_jet_pt[1] < 30 ) \
             && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13)   \
             && fabs(91.1876 - mll) < 7.5 \
             && ( std_vector_jet_pt[0] < 20 || std_vector_jet_cmvav2[0] < -0.715 ) \
             && ( std_vector_jet_pt[1] < 20 || std_vector_jet_cmvav2[1] < -0.715 ) \
             && ( std_vector_jet_pt[2] < 20 || std_vector_jet_cmvav2[2] < -0.715 ) \
             && ( std_vector_jet_pt[3] < 20 || std_vector_jet_cmvav2[3] < -0.715 ) \
             && ( std_vector_jet_pt[4] < 20 || std_vector_jet_cmvav2[4] < -0.715 ) \
             && ( std_vector_jet_pt[5] < 20 || std_vector_jet_cmvav2[5] < -0.715 ) \
             && ( std_vector_jet_pt[6] < 20 || std_vector_jet_cmvav2[6] < -0.715 ) \
             && ( std_vector_jet_pt[7] < 20 || std_vector_jet_cmvav2[7] < -0.715 ) \
             && ( std_vector_jet_pt[8] < 20 || std_vector_jet_cmvav2[8] < -0.715 ) \
             && ( std_vector_jet_pt[9] < 20 || std_vector_jet_cmvav2[9] < -0.715 ) \
             && dymvaggh > 0.95 \
               '

