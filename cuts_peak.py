# cuts

#cuts = {}
  
#std_vector_lepton_isTightLepton[2] == 1 \ not defined anymore Oct 2017
            #&& mllmin3l > 76. && mllmin3l < 106. \

supercut = ' PuppiMET_pt > 30  \
           '

cuts['ZTomumuWTomu']  = ' Lepton_pt[0] > 40 && Lepton_pt[1] > 40 && Lepton_pt[2] > 40 && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13 \
             '   
cuts['ZTomumuWToe']  = ' Lepton_pt[0] > 30 && Lepton_pt[1] > 40 && Lepton_pt[2] > 40 && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*11  \
              '  
cuts['ZTomumu']  = ' Lepton_pt[0] > 30 && Lepton_pt[1] > 30 && Lepton_pt[2] > 30 && (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*13) || (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 13*13*11)  \
               ' 
cuts['ZToeeWTomu']  = 'Lepton_pt[0] > 40  && Lepton_pt[1] > 30 && Lepton_pt[2] > 30 &&  fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13 \
                '
cuts['ZToeeWToe']  = 'Lepton_pt[0] > 30 && Lepton_pt[1] > 30 && Lepton_pt[2] > 30 && fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11 \
                '
cuts['ZToee']  = 'Lepton_pt[0] > 30 && Lepton_pt[1] > 30 && Lepton_pt[2] > 30 && (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*13) || (fabs(Lepton_pdgId[0] * Lepton_pdgId[1] * Lepton_pdgId[2])== 11*11*11) \
                 '
