import cv2, glob, os
import numpy as np
import matplotlib.pyplot as plt

def xy_Slices(path):
	directory = "/".join(path.split('/')[:-1])
	extension = path.split('/')[-1].split('.')[1]
	file_name = path.split('/')[-1].split('.')[0]

	image = cv2.imread(path, 0)
	plot, ax = plt.subplots()

	height, width = image.shape
	print("Height\t:\t", height, "\t\tWidth\t:\t", width)

	if not os.path.exists(directory + "/Slices/"):
		os.makedirs(directory + "/Slices/")

	for x in range(height):
		if(image[x].sum() / 255 > 750):
			ax.axhline(y = x, linewidth=2, color='black')

	ax.imshow(image, cmap='gray')
	plot.savefig(directory + "/Slices/Slice_" + file_name.split('/')[-1].split('.')[0] + ".png", dpi = 100)

def main():
	xy_Slices("../lab3 Images/XY-cutss.png")

if __name__ == '__main__':
	main()