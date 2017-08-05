



def han_grid_spacing(size, itemCount, w, h):
    spacingDict = {}
    
    gridSizeCfg = [1,4,8,16]
    gridDict    = {1:(0,0), 4:(2,2), 8:(4,2) ,16:(4,4)}
    
    if size == 1:
        spacingDict = {}
        spacingDict[0] = {'x':(w/2)/2,'y':0,'w':h,'h':h}                              
        return spacingDict[0]
    
    c, r = gridDict[size]
    
    objW = int(w/c)
    objH = int(h/r)
    print(objH)
    
    item = 0
    prevX = 0
    for k in range(0,r):
        y = k*objH
        for i in range(0,c):
            w = objW
            if i == 0:
                x = objH/2
                prevX = x
            else:
                x = prevX+objH
                prevX = x
            spacingDict[item] = {'x':x,'y':y,'w':objH,'h':objH}
            item += 1
     
    return spacingDict[itemCount]
    
    
    
    def han_grid_spacing(self, size, itemCount, w, h):
        spacingDict = {}
        
        if size == 1:
            spacingDict = {}
            spacingDict[0] = {'x':0,'y':0,'w':w,'h':h}
            return spacingDict[0]
        
        c, r = self.gridDict[size]
        
        objW = int(w/c)
        objH = int(h/r)
        
        item = 0
        for k in range(0,r):
            y = k*objH
            for i in range(0,c):
                w = objW
                x = i*objW
                spacingDict[item] = {'x':x,'y':y,'w':w,'h':objH}
                item += 1
 
        return spacingDict[itemCount]

han_grid_spacing(4, 0, 1920, 1080)