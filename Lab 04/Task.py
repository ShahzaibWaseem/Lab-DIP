import cv2, os
import matplotlib.pyplot as plt
import numpy as np

IMAGE_PATH = "Image/Fruits.png"

def Binarization(image, filename):
	retval, binarized_img = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
	cv2.imwrite(filename, binarized_img)

	return binarized_img

def FirstPass(image, height, width):
	CURRENT_LABEL = 1
	labels = np.zeros( (height, width), dtype=np.uint8 )
	prefernces = {}

	for x in range(height):
		for y in range(width):
			# dealing with background
			if image[x, y] == 255:
				continue

			above = image[x-1, y]
			left = image[x, y-1]
			# if both above and left are 0; New Label
			if above == 0 and left == 0:
				labels[x, y] = CURRENT_LABEL
				CURRENT_LABEL += 1

			# if both not 0 ; choose left
			if above != 0 and left != 0:
				labels[x, y] = min(labels[x-1, y], labels[x, y-1])
				prefernces[max(labels[x-1, y], labels[x, y-1])] = min(labels[x-1, y], labels[x, y-1])

			# if either not 0
			if above > 0 and left == 0:
				labels[x, y] = labels[x-1, y]
			if above == 0 and left > 0:
				labels[x, y] = labels[x, y-1]

	plt.imshow(labels, cmap="nipy_spectral")
	plt.show()

	return labels, prefernces

def SecondPass(image, prefernces, height, width):
	for x in range(height):
		for y in range(width):
			above = image[x-1, y]
			left = image[x, y-1]

			# Dictionary Matching
			try:
				labels[x, y] = prefernces[labels[x, y]]
			except Exception as e:
				continue

	plt.imshow(image, cmap="nipy_spectral")
	plt.show()

def main():
	image = cv2.imread(IMAGE_PATH, 0)
	cv2.imshow("RGB Image", image)
	cv2.waitKey(0)

	directory = "/".join(IMAGE_PATH.split('/')[:-1])
	extension = IMAGE_PATH.split('/')[-1].split('.')[1]
	file_name = IMAGE_PATH.split('/')[-1].split('.')[0]

	if not os.path.exists(directory + "/Binarized/"):
		os.makedirs(directory + "/Binarized/")

	grayscale = Binarization(image, directory + "/Binarized/" + "bin_" + file_name + "." + extension)

	height, width = grayscale.shape
	print("Height\t:\t" + str(height) + "\t\tWidth\t:\t" + str(width))

	labels , prefernces = FirstPass(grayscale, height, width)
	SecondPass(labels, prefernces, height, width)

if __name__ == '__main__':
	main()