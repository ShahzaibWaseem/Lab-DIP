import sys, PIL
from PIL import Image

file = sys.argv[1]
img = Image.open(file)
try:
	jpg_img = img.convert('RGB')
	jpg_img.save(file.split('.')[0] + '.jpg')
	print "Image", file, "Converted to", file.split('.')[0] + '.jpg'
	jpg_img.show()
except IOError:
	print "Cannot Convert", file