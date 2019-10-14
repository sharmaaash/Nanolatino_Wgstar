# cuts

#cuts = {}
  
supercut = 'Lepton_pt[0]>25 && Lepton_pt[1]>8 \
         && Lepton_pt[2]>8 \
'


#
         #&& MET_pt < 50 \

         #&& Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1 \



cuts['mmm_TGGmpmet_NoJpsi']  = ' Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 &&  Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mpmet > 25 && abs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2]) == 13*13*13 && mllTwoThree > 0 && abs( mllTwoThree - 3.1) > 0.1'

cuts['emm_TGGmpmet_NoJpsi']  = ' Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5 &&  Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mpmet > 25 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]*Lepton_pdgId[2]) == 11*13*13 && mllTwoThree > 0 && abs(  mllTwoThree -3.1) > 0.1 '

cuts['eem_TGGmpmet_NoJpsi']  = ' Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 &&  Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mpmet > 25 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]*Lepton_pdgId[2])==11*11*13  && mllTwoThree > 0 && abs(  mllTwoThree -3.1) > 0.1'

cuts['eee_TGGmpmet_NoJpsi']  = ' Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5 &&  Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mpmet > 25 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]*Lepton_pdgId[2]) == 11*11*11 && mllTwoThree > 0 && abs(  mllTwoThree -3.1) > 0.1 '


# mtw2 > 30 at ggH


cuts['mmm_TGGmtw2_NoJpsi']  = ' Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 &&  Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mtw2 > 30 && abs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2]) == 13*13*13 && mllTwoThree > 0 && abs( mllTwoThree - 3.1) > 0.1'

cuts['emm_TGGmtw2_NoJpsi']  = ' Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5 &&  Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mtw2 > 30 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]*Lepton_pdgId[2]) == 11*13*13 && mllTwoThree > 0 && abs(  mllTwoThree -3.1) > 0.1 '

cuts['eem_TGGmtw2_NoJpsi']  = ' Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5 && Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mtw2 > 30 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]*Lepton_pdgId[2])==11*11*13  && mllTwoThree > 0 && abs(  mllTwoThree -3.1) > 0.1'

cuts['eee_TGGmtw2_NoJpsi']  = ' Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5 && Lepton_isWgs[1] > 0.5 && Lepton_isWgs[2] > 0.5 && mtw2 > 30 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]*Lepton_pdgId[2]) == 11*11*11 && mllTwoThree > 0 && abs(  mllTwoThree -3.1) > 0.1 '



#Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5
#Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5


# 11 = e
# 13 = mu
# 15 = tau
