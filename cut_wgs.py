
supercut = 'Lepton_pt[0]>30 && Lepton_pt[1]>6 && Lepton_pt[2]>6 && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 \
             '




#cuts['ZTommWTom_mpmet']  = ' mpmet > 25 \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])==13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 &&  fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5'


cuts['ZTommWToe_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5  '

#cuts['ZTommWToe_mpmet']  = ' mpmet > 25  \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTomm_mpmet']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5  '


cuts['ZToeeWTom_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5  '

cuts['ZTomm_mpmet_WgSt']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1 &&  mllTwoThree < 4. && mllTwoThree >0. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5  '


cuts['ZTomm_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5  '

#cuts['ZToeeWTomu_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTommWToe_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5  '

#cuts['ZToee_mpmet']  = ' mpmet > 25 \
#                      && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13) || (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '


#cuts['ZTommWTom_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTommWToe_MET_pt']  = '  MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTomm_MET_pt']  = ' MET_pt > 25 \
              && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11|| (Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*13)) && fabs( mllTwoThree - 3.1) > 0.1 '

#cuts['ZToeeWTomu_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
#cuts['ZTommWTom_mpmet']  = ' mpmet > 25 \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])==13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 &&  fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5'


cuts['ZTommWToe_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZTommWToe_mpmet']  = ' mpmet > 25  \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTomm_mpmet']  = '  mpmet > 25  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 && Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 && Lepton_isTightMuon_cut_Tight_HWWW[1]>0.5 && Lepton_isTightMuon_cut_Tight_HWWW[2]>0.5 '


cuts['ZToeeWTom_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZTomm_mpmet_WgSt']  = '  mpmet > 25  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1 &&  mllTwoThree < 4. && mllTwoThree >0. && Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '


cuts['ZTomm_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZToeeWTomu_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTommWToe_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZToee_mpmet']  = ' mpmet > 25 \
#                      && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13) || (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '


#cuts['ZTommWTom_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTommWToe_MET_pt']  = '  MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTomm_MET_pt']  = ' MET_pt > 25 \
#              && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '

#cuts['ZToeeWTomu_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
#cuts['ZTommWTom_mpmet']  = ' mpmet > 25 \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])==13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 &&  fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5'


cuts['ZTommWToe_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZTommWToe_mpmet']  = ' mpmet > 25  \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTomm_mpmet']  = '  mpmet > 25  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 && Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 && Lepton_isTightMuon_cut_Tight_HWWW[1]>0.5 && Lepton_isTightMuon_cut_Tight_HWWW[2]>0.5 '


cuts['ZToeeWTom_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZTomm_mpmet_WgSt']  = '  mpmet > 25  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1 &&  mllTwoThree < 4. && mllTwoThree >0. && Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '


cuts['ZTomm_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZToeeWTomu_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTommWToe_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZToee_mpmet']  = ' mpmet > 25 \
#                      && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13) || (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '


#cuts['ZTommWTom_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTommWToe_MET_pt']  = '  MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTomm_MET_pt']  = ' MET_pt > 25 \
#              && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '

#cuts['ZToeeWTomu_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '
#cuts['ZTommWTom_mpmet']  = ' mpmet > 25 \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])==13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 &&  fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5'


cuts['ZTommWToe_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZTommWToe_mpmet']  = ' mpmet > 25  \
#                            && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTomm_mpmet']  = '  mpmet > 25  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 && Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 && Lepton_isTightMuon_cut_Tight_HWWW[1]>0.5 && Lepton_isTightMuon_cut_Tight_HWWW[2]>0.5 '


cuts['ZToeeWTom_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZTomm_mpmet_WgSt']  = '  mpmet > 25  \
#                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1 &&  mllTwoThree < 4. && mllTwoThree >0. && Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '


cuts['ZTomm_mpmet_WgSt_gt0p1']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 3.1) > 0.1  && mllTwoThree < 4. && mllTwoThree >0.1 && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZToeeWTomu_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_mpmet']  = ' mpmet > 25 \
#                          && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

cuts['ZTommWToe_mpmet_Zpeak']  = '  mpmet > 25  \
                          && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13)) && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && fabs(mllTwoThree - 91.2) < 10. && Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 '

#cuts['ZToee_mpmet']  = ' mpmet > 25 \
#                      && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13) || (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '


#cuts['ZTommWTom_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTommWToe_MET_pt']  = '  MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*13*13 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZTomm_MET_pt']  = ' MET_pt > 25 \
#              && ((fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11)) && fabs( mllTwoThree - 3.1) > 0.1 '

#cuts['ZToeeWTomu_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5 || Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

#cuts['ZToeeWToe_MET_pt']  = ' MET_pt > 25 \
#              && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 && (Lepton_pdgId[1] * Lepton_pdgId[2] < 0) && mllTwoThree > 0 && fabs(mllTwoThree - 3.1) > 0.1 && (Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]>0.5 '

