# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }

variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',            #   variable name    
                        'range' : (20,0.,200),    #   variable range
                        'xaxis' : 'lept1_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }
    
variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',            #   variable name    
                        'range' : (20,0.,200),    #   variable range
                        'xaxis' : 'lept2_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['pt3']  = {   'name': 'std_vector_lepton_pt[2]',            #   variable name    
                        'range' : (20,0.,200),    #   variable range
                        'xaxis' : 'lept3_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }

#variables['flagOSSF']  = {   'name': 'flagOSSF',            #   variable name    
#                        'range' : (2,0,2),    #   variable range
#                        'xaxis' : 'flag OSSF',  #   x axis name
#                         'fold' : 0
#                        }
#
variables['zveto_3l']  = {   'name': 'zveto_3l',            #   variable name    
                        'range' : (20,0,100),    #   variable range
                        'xaxis' : 'm_{ll} - M_{Z} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['drllmin3l']  = {   'name': 'drllmin3l',            #   variable name    
                         'range' : (6,0,4),    #   variable range
                         'range' : ([0.,0.75, 1.5, 2.0, 2.5, 4.0],),    #   variable range
                      #   'range' : ([0.,0.5,1.0,1.5,2.0,3.0,4.0],),    #   variable range
                         'xaxis' : 'min #Delta R_{ll}',  #   x axis name
                         'fold' : 0
                        }

variables['drllmin3l_sssf']  = {   'name': 'drllmin3l',            #   variable name    
                        'range' : (3,0,4),    #   variable range
                      #   'range' : ([0.,1.1,1.7,2.5,4.0],),    #   variable range
                        'xaxis' : 'min #Delta R_{ll}',  #   x axis name
                         'fold' : 0
                        }

variables['mllmin3l']  = {   'name': 'mllmin3l',            #   variable name    
                       'range' : (10,10,100),    #   variable range
                        'xaxis' : 'min m_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }


variables['mlll']  = {   'name': 'mlll',            #   variable name    
                        'range' : (50,0.,500),    #   variable range
                        'xaxis' : 'm_{lll} [GeV]',  #   x axis name
                        'fold' : 0
                        }
 


##variables['mllVSdrll'] = {   'name': 'mllmin3l:drllmin3l',            #   variable name    
##                        'range' : (6,0.,4., 10,10,100),            #   variable range
##                        'xaxis' : 'min #Delta R_{ll} :  min m_{ll}',      #   x axis name
##                        'fold' : 3 ,
##                        # do weighted plot too
##                        'doWeight' : 1,
##                        'binX'     : 6,
##                        'binY'     : 10
##                        #
##                        }
##
#                       
#variables['nvtx']  = {   'name': 'nvtx',      
#                        'range' : (40,0,40),  
#                        'xaxis' : 'nvtx', 
#                         'fold' : 3
#                        }
#                        
###
variables['met']  = {   'name': 'metPfType1',            #   variable name    
                        'range' : (10,0,200),    #   variable range
                        'xaxis' : 'pfmet [GeV]',  #   x axis name
                       'fold' : 0
                    }

variables['mtwww']  = {   'name': 'mtwww',            #   variable name    
                        'range' : (20,0,500),    #   variable range
                        'xaxis' : 'mT_WWW [GeV]',  #   x axis name
                       'fold' : 0
                     }


variables['minmtw_wh3l']  = {   'name': 'minmtw_wh3l',            #   variable name    
                        'range' : (20,0,200),    #   variable range
                        'xaxis' : 'min mT_W [GeV]',  #   x axis name
                       'fold' : 0
                     }

variables['ptlll']  = {   'name': 'ptlll',            #   variable name    
                        'range' : (20,0,500),    #   variable range
                        'xaxis' : 'pT_lll [GeV]',  #   x axis name
                       'fold' : 0
                     }

variables['pTWWW']  = {   'name': 'pTWWW',            #   variable name    
                        'range' : (20,0,500),    #   variable range
                        'xaxis' : 'pT_WWW [GeV]',  #   x axis name
                       'fold' : 0
                     }

variables['mindphi_lmet']  = {   'name': 'mindphi_lmet',            #   variable name    
                        'range' : (10,0.,3.5),    #   variable range
                        'xaxis' : 'min #Delta#Phi(l,MET)',  #   x axis name
                       'fold' : 0
                     }

variables['dphilllmet']  = {   'name': 'dphilllmet',            #   variable name    
                        'range' : (10,0.,3.5),    #   variable range
                        'xaxis' : 'min #Delta#Phi(lll,MET)',  #   x axis name
                       'fold' : 0
                     }
