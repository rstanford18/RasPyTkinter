import pickle
import GlobalFunctions as gf
import GlobalVariables as gv

###############################################################################
def saveTagFile():
    with open(gv.TagElementPath, 'wb') as handle:
        pickle.dump(gv.tagElements, handle)
        print('Tag Element Save',gv.tagElements)
###############################################################################
def loadTagFile():
    try:
        with open(gv.TagElementPath, 'rb') as handle:
            gv.tagElements = pickle.loads(handle.read())
    except:
        print('Pickle failed to load Tag Omf.')
###############################################################################

def saveCamFile():
    with open(gv.CamElementPath, 'wb') as handle:
        pickle.dump(gv.camElements, handle)
        print('Cam Element Save',gv.camElements)
###############################################################################
def loadCamFile():
    try:
        with open(gv.CamElementPath, 'rb') as handle:
            gv.camElements = pickle.loads(handle.read())
    except:
        print('Pickle failed to load Cam Omf.')