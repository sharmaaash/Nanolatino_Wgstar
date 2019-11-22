






supercut = ' Lepton_pt[0] > 30 && abs(mll - 3.1) > 0.1  \
              '

#cuts['ZToeeWTom_mpmet_Zpeak']  = '  mpmet > 30  \
#                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 ) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
#cuts['ZTommWToe_mpmet_Zpeak']  = '  mpmet > 30  \
#                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. &&  (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) &&  Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
#
#cuts['ZToeeWTom_met_Zpeak']  = '  MET_pt > 30  \
#                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 ) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
#cuts['ZTommWToe_met_Zpeak']  = '  MET_pt > 30  \
#                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && ( Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
#
#cuts['ZToeeWToe_mpmet_Zpeak']  = '  mpmet > 30  \
#                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
#cuts['ZTommWTom_mpmet_Zpeak']  = '  mpmet > 30  \
#                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '


#cuts['ZToeeWToe_met_Zpeak']  = '  MET_pt > 30  \
#                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
#cuts['ZTommWTom_met_Zpeak']  = '  MET_pt > 30  \
#                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTommWToe_puppiMET']  = ' PuppiMET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '
#cuts['ZTommWToe']  = '   Lepton_pt[0] > 30 && Lepton_pt[1] > 40 && Lepton_pt[2] > 40  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
cuts['ZTommWToe_mpmet']  = ' mpmet > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 ) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '
#cuts['ZToeeWToe']  = '    Lepton_pt[0] > 30 && Lepton_pt[1] > 30 && Lepton_pt[2] > 30  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
#cuts['ZTommWTom']  = '   Lepton_pt[0] > 40 && Lepton_pt[1] > 40 && Lepton_pt[2] > 40  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
cuts['ZTommWToe_mtw']  = ' mtw1 > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '

cuts['ZTommWToe_met']  = ' MET_pt > 30\
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0)  && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 && fabs(mllTwoThree - 3.1) > 0.1 '
