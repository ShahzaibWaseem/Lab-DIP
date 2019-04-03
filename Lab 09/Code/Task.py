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

def medianSmoothing(image, windowSize):
	height, width = image.shape
	padSize = windowSize // 2		# Integer Division
	newImage = np.zeros(image.shape)
	image = np.pad(image, (padSize, padSize), 'constant', constant_values=(0) )

	for x in range(padSize, height - padSize):
		for y in range(padSize, width - padSize):
			pixels = image[x-padSize:x+padSize+1, y-padSize:y+padSize+1]
			pixels = np.sort(pixels, axis=None)
			newImage[x-padSize, y-padSize] = pixels[(windowSize**2) // 2]
	return newImage

def main():
	IMAGE_PATH = "../Images/"
	smoothing_image = "saltandpaper.tif"
	# windowSize = 7			# Change this to whatever filter you require

	image = cv2.imread(IMAGE_PATH + smoothing_image, 0)
	# Task 1a Filter
	# filter = np.ones((windowSize, windowSize)) / (windowSize * windowSize)

	# Task 1b Filter
	# filter = np.array([ [1, 2, 1], [2, 4, 2], [1, 2, 1] ], np.int32) / 16

	# Task 2 Filter
	# sigma = 1.4
	# gaussianFilter = np.array([ [1, 1, 2, 2, 2, 1, 1],
	# 							[1, 2, 2, 4, 2, 2, 1],
	# 							[2, 2, 4, 8, 4, 2, 2],
	# 							[2, 4, 8,16, 8, 4, 2],
	# 							[2, 2, 4, 8, 4, 2, 2],
	# 							[1, 2, 2, 4, 2, 2, 1],
	# 							[1, 1, 2, 2, 2, 1, 1] ], np.float)
	# gaussianFilter = gaussianFilter / np.sum(gaussianFilter * sigma)

	# Task 3 Filter
	# filter = np.array([ [1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.int32)
	# filter = np.ones((windowSize, windowSize))

	# newImage = Smoothening(image, filter)
	# newImage = image + (image - newImage)

	newImage = medianSmoothing(image, 3)	# Filter Size = 3x3

	stackedImage = np.hstack((image, newImage))
	cv2.imwrite(IMAGE_PATH + "output " + smoothing_image.split(".")[0] + ".png", newImage)

	plt.imshow(stackedImage, cmap='gray')
	plt.show()

if __name__ == '__main__':
	main()