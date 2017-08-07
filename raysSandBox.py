import GlobalFunctions as gf

yList = []
for i in range(16):
    if i == 0:
        z = 5
    else:
        z = yList[-1]+35              
    yList.append(z)
    
    
gf.ppr(yList)