import matplotlib.pyplot as plt
import numpy as np
import cv2

def Smoothening(image, filter):
	height, width = image.shape
	windowSize = filter.shape[1]
	padSize = windowSize // 2		# Integer Division

	newImage = np.zeros(image.shape)
	filterSum = np.sum(filter)
	image = np.pad(image, (padSize, padSize), 'constant', constant_values=(0) )

	for x in range(padSize, height - padSize):
		for y in range(padSize, width - padSize):
			pixels = image[x-padSize:x+padSize+1, y-padSize:y+padSize+1]
			newImage[x-padSize,y-padSize] = np.sum(np.multiply(pixels, filter/filterSum))
	return newImage

def main():
	IMAGE_PATH = "../Images/"
	smoothing_image = "smoothing.tif"
	windowSize = 3			# Change this to whatever filter you require

	image = cv2.imread(IMAGE_PATH + smoothing_image, 0)
	filter = np.ones((windowSize, windowSize)) / (windowSize * windowSize)
	newImage = Smoothening(image.copy(), filter)

	stackedImage = np.hstack((image, newImage))
	cv2.imwrite(IMAGE_PATH + str(windowSize) + "x" + str(windowSize) + smoothing_image.split(".")[0] + ".png", newImage)

	plt.imshow(stackedImage, cmap='gray')
	plt.show()

if __name__ == '__main__':
	main()