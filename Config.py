import pickle
import GlobalFunctions as gf
import GlobalVariables as gv

###############################################################################
def saveConfigFile():
    with open(gv.configFile, 'wb') as handle:
        pickle.dump(gv.tagElements, handle)
        print('Config Save',gv.tagElements)
###############################################################################
def loadConfigFile():
    try:
        with open(gv.configFile, 'rb') as handle:
            gv.tagElements = pickle.loads(handle.read())
    except:
        print('Pickle failed to load INI.')
###############################################################################