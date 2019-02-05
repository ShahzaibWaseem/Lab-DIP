import sys, PIL
from PIL import Image
from PIL import ImageFilter

file = sys.argv[1]
img = Image.open(file)
img.show()
try:
	jpg_img = img.convert('L')
	outFileName = 'Grayscale_'+ file.split('.')[0] +'.jpg'
	jpg_img.save(outFileName)
	print "Grayscale"
	print "Image", file, "Converted to", outFileName
	jpg_img.show()
except IOError:
	print "Cannot Convert", file