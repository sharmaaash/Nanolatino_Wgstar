


supercut = 'Lepton_pt[0]>30 && Lepton_pt[1]>8 && Lepton_pt[2]>8 \
              '


cuts['hww2l2v_13TeV_WgS_mmm_met']  = ' \
                   abs(Lepton_pdgId[0]) == 13 \
                && abs(Lepton_pdgId[1]) == 13   \
                && abs(Lepton_pdgId[2]) == 13   \
                && abs(Lepton_eta[0])<2.4 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && (Lepton_isTightMuon_cut_Tight_HWWW[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && MET_pt > 25 \
                '

cuts['hww2l2v_13TeV_WgS_mee_met']  = ' \
                   abs(Lepton_pdgId[0]) == 13 \
                && abs(Lepton_pdgId[1]) == 11   \
                && abs(Lepton_pdgId[2]) == 11   \
                && abs(Lepton_eta[0])<2.4 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && ( Lepton_isTightMuon_cut_Tight_HWWW[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && MET_pt > 25 \
                '

cuts['hww2l2v_13TeV_WgS_emm_met']  = ' \
                   abs(Lepton_pdgId[0]) == 11 \
                && abs(Lepton_pdgId[1]) == 13   \
                && abs(Lepton_pdgId[2]) == 13   \
                && abs(Lepton_eta[0])<2.1 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && MET_pt > 25 \
                '


cuts['hww2l2v_13TeV_WgS_eee_met']  = ' \
                   abs(Lepton_pdgId[0]) == 11 \
                && abs(Lepton_pdgId[1]) == 11   \
                && abs(Lepton_pdgId[2]) == 11   \
                && abs(Lepton_eta[0])<2.1  \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && MET_pt > 25 \
                '


cuts['hww2l2v_13TeV_WgS_mmm_mpmet']  = ' \
                   abs(Lepton_pdgId[0]) == 13 \
                && abs(Lepton_pdgId[1]) == 13   \
                && abs(Lepton_pdgId[2]) == 13   \
                && abs(Lepton_eta[0])<2.4 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && (Lepton_isTightMuon_cut_Tight_HWWW[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mpmet > 25 \
                '

cuts['hww2l2v_13TeV_WgS_mee_mpmet']  = ' \
                   abs(Lepton_pdgId[0]) == 13 \
                && abs(Lepton_pdgId[1]) == 11   \
                && abs(Lepton_pdgId[2]) == 11   \
                && abs(Lepton_eta[0])<2.4 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && ( Lepton_isTightMuon_cut_Tight_HWWW[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mpmet > 25 \
                '

cuts['hww2l2v_13TeV_WgS_emm_mpmet']  = ' \
                   abs(Lepton_pdgId[0]) == 11 \
                && abs(Lepton_pdgId[1]) == 13   \
                && abs(Lepton_pdgId[2]) == 13   \
                && abs(Lepton_eta[0])<2.1 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mpmet > 25 \
                '


cuts['hww2l2v_13TeV_WgS_eee_mpmet']  = ' \
                   abs(Lepton_pdgId[0]) == 11 \
                && abs(Lepton_pdgId[1]) == 11   \
                && abs(Lepton_pdgId[2]) == 11   \
                && abs(Lepton_eta[0])<2.1  \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mpmet > 25 \
                '

cuts['hww2l2v_13TeV_WgS_mmm_mtw']  = ' \
                   abs(Lepton_pdgId[0]) == 13 \
                && abs(Lepton_pdgId[1]) == 13   \
                && abs(Lepton_pdgId[2]) == 13   \
                && abs(Lepton_eta[0])<2.4 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && (Lepton_isTightMuon_cut_Tight_HWWW[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mtw2 > 25 \
                '

cuts['hww2l2v_13TeV_WgS_mee_mtw2']  = ' \
                   abs(Lepton_pdgId[0]) == 13 \
                && abs(Lepton_pdgId[1]) == 11   \
                && abs(Lepton_pdgId[2]) == 11   \
                && abs(Lepton_eta[0])<2.4 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && ( Lepton_isTightMuon_cut_Tight_HWWW[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mtw2 > 25 \
                '

cuts['hww2l2v_13TeV_WgS_emm_mtw2']  = ' \
                   abs(Lepton_pdgId[0]) == 11 \
                && abs(Lepton_pdgId[1]) == 13   \
                && abs(Lepton_pdgId[2]) == 13   \
                && abs(Lepton_eta[0])<2.1 \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1) && Lepton_isWgs[1]==1 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mtw2 > 25 \
                '


cuts['hww2l2v_13TeV_WgS_eee_mtw2']  = ' \
                   abs(Lepton_pdgId[0]) == 11 \
                && abs(Lepton_pdgId[1]) == 11   \
                && abs(Lepton_pdgId[2]) == 11   \
                && abs(Lepton_eta[0])<2.1  \
                && Lepton_pdgId[1]*Lepton_pdgId[2]<0   \
                && mllTwoThree > 0 \
                && (Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]==1) && Lepton_isWgs[1]>0.5 && Lepton_isWgs[2]==1 \
                &&  fabs(mllTwoThree - 3.1) > 0.1 \
                && mtw2 > 25 \
                '


