class GeoMgr():

    def __init__(self):
        self.gridSizeCfg = [1,4,8,16]
        self.gridDict    = {1:(0,0), 4:(2,2), 8:(4,2) ,16:(4,4)}
        
    def han_grid_spacing(self, size, itemCount, w, h):
        spacingDict = {}
        oriH = h
        if size == 1:
            spacingDict = {}
            spacingDict[0] = {'x':(w/2)/2,'y':0,'w':h,'h':h}                              
            return spacingDict[0]
        
        c, r = self.gridDict[size]
        xPadStart = 200
        pw = w-(xPadStart*2)
        
        #Lets figure out the area we are working with.
        colSquare = int(pw/c)
        rowSquare = int(h/r)
        
        w = min(colSquare,rowSquare)
        h = w
        yOffset = (oriH - (h*r))/2
        xPadStart = xPadStart+((pw-(c*w))/2)
        print(xPadStart)
        item = 0
        prevX = 0
        for k in range(0,r):
            y = (k*h)+yOffset
            for i in range(0,c):
                if i == 0:
                    x = xPadStart
                    prevX = x
                else:
                    x = prevX+w
                    prevX = x
                spacingDict[item] = {'x':x, 'y':y, 'w':w, 'h':h}
                item += 1
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(spacingDict)
        return spacingDict[itemCount]
        
        
g = GeoMgr()
g.han_grid_spacing(16, 1, 1910, 1055)