# example of configuration file

tag = 'monoHWW'


# used by mkShape to define output directory for root files
outputDir = 'rootFile'


# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 



# luminosity to normalize to (in 1/fb)
# lumi = 2.264
lumi = 12.9
#lumi = 100.0


# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'
#outputDirDatacard = '100datacards'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
#nuisancesFile = 'nuisances_light.py'
nuisancesFile = 'nuisances.py'


