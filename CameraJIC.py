import numpy
from PIL import Image
 
# Convert Image to array
img = Image.open("C:\\Users\\RaymondS\\git\\offline.jpg").convert("L")
arr = numpy.array(img)
 
# Convert array to Image
img = Image.fromarray(arr)
print(img)

numpy.set_printoptions(threshold=numpy.inf)
print(arr)