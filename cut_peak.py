






supercut = 'Lepton_pt[0]>20 && Lepton_pt[1]>20 && Lepton_pt[2]>20 \
              '

cuts['ZToeeWTom_mpmet_Zpeak']  = '  mpmet > 30  \
                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 ) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
cuts['ZTommWToe_mpmet_Zpeak']  = '  mpmet > 30  \
                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. &&  (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) &&  Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

cuts['ZToeeWTom_met_Zpeak']  = '  MET_pt > 30  \
                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 ) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
cuts['ZTommWToe_met_Zpeak']  = '  MET_pt > 30  \
                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && ( Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

cuts['ZToeeWToe_mpmet_Zpeak']  = '  mpmet > 30  \
                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
cuts['ZTommWTom_mpmet_Zpeak']  = '  mpmet > 30  \
                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '


cuts['ZToeeWToe_met_Zpeak']  = '  MET_pt > 30  \
                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
cuts['ZTommWTom_met_Zpeak']  = '  MET_pt > 30  \
                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZToeeWTom_mtw_Zpeak']  = '   mtw2 > 30  \
                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 ) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '
cuts['ZTommWToe_mtw_Zpeak']  = '   mtw2 > 30  \
                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

cuts['ZToeeWToe_mtw_Zpeak']  = '   mtw2 > 30  \
                          && abs(Lepton_eta[0])<2.1 && abs(Lepton_eta[1])<2.1 && abs(Lepton_eta[2])<2.1 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
cuts['ZTommWTom_mtw_Zpeak']  = '   mtw2 > 30  \
                          && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 && abs(Lepton_eta[2])<2.4 \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '



