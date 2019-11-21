#!/bin/python

from ROOT import *

inFile = TFile("rootFile/plots_Top1jet.root")
#inFile = TFile("rootFile/plots_TopNoSF.root")

#inFile.cd("TopCtrl1jet/events")
inFile.cd("hww2l2v_13TeV_top_of1j/events")

top=0
data=0
bkg=0

for key in gDirectory.GetListOfKeys():
  name = key.GetTitle()
  print name
  if "Up" in name or "Down" in name or "stat" in name or "ibin" in name: continue

  h = gDirectory.Get(name)
  print name," : ",h.Integral() 

  if name=="histo_ttbar" or name=="histo_ST" or name=="histo_top":
    top+=h.Integral()/3.
  elif name=="histo_DATA":
    data+=h.Integral()
    D_data = h.GetBinError(1) 
  else:
    bkg+=h.Integral()/3.
  
k = (data - bkg)/top
D_k = D_data/top

print "k = ", k, " +/- ", D_k

