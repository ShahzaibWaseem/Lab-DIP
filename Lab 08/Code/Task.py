import cv2
import matplotlib.pyplot as plt
import numpy as np

def HistogramEqualization(image):
	height, width = image.shape
	N = height*width
	image_pixel = np.zeros(image.shape)
	newImage = np.zeros(image.shape)

	for x in range(height):
		for y in range(width):
			image_pixel[image[x,y]] += 1

	image_pixel, values = np.histogram(image.flatten(), 256, [0, 256])
	prob_dist = ((256 - 1) * image_pixel) / image.size
	cumm_dist = prob_dist.cumsum()

	for x in range(256):
		newImage[x] = cumm_dist[x] * 255

	for x in range(height):
		for y in range(width):
			newImage[x,y] = cumm_dist[image[x,y]]

	return newImage

def TilingApproach(image):
	height, width = image.shape
	tileX, tileY = height//2, width//2

	print("height, Width: \t", height, width)
	print("TileX, TileY: \t", tileX, tileY)

	# HISTOGRAMS
	plt.hist(image.ravel(), 256, [0,256])
	plt.savefig("../Images/originalImage_Histogram.png")
	plt.show()

	print("Top Left:\t", 0, "\t", tileX, "\t", 0, "\t", tileY)
	print("Bottom Left:\t", tileX, "\t", width, "\t", 0, "\t", tileY)
	print("Top Right:\t", 0, "\t", tileX, "\t", tileY, "\t", height)
	print("Bottom Right:\t", tileX, "\t", width, "\t", tileY, "\t", height)

	cv2.imshow("Before Local Enhancement", image)
	cv2.waitKey(0)

	image[0: tileX, 0: tileY] = HistogramEqualization(image[0: tileX, 0: tileY])
	image[tileX: width, 0: tileY] = HistogramEqualization(image[tileX: width, 0: tileY])
	image[0: tileX, tileY: height] = HistogramEqualization(image[0: tileX, tileY: height])
	image[tileX: width, tileY: height] = HistogramEqualization(image[tileX: width, tileY: height])

	plt.hist(image[0: tileX, 0: tileY].ravel(), 256, [0,256])
	plt.savefig("../Images/Tile/localEqualization_Histogram(lt).png")
	plt.show()
	plt.hist(image[tileX: width, 0: tileY].ravel(), 256, [0,256])
	plt.savefig("../Images/Tile/localEqualization_Histogram(bl).png")
	plt.show()
	plt.hist(image[0: tileX, tileY: height].ravel(), 256, [0,256])
	plt.savefig("../Images/Tile/localEqualization_Histogram(tr).png")
	plt.show()
	plt.hist(image[tileX: width, tileY: height].ravel(), 256, [0,256])
	plt.savefig("../Images/Tile/localEqualization_Histogram(br).png")
	plt.show()

	cv2.imshow("After Local Enhancement", image)
	cv2.waitKey(0)

	plt.hist(image.ravel(), 256, [0,256])
	plt.savefig("../Images/localEqualization_Histogram.png")
	cv2.imwrite("../Images/localEqualization_Image.png", image)

def SlidingWindowApproach(image, window):
	height, width = image.shape
	newImage = np.zeros((image.shape))

	print("height, Width:\t", height, width)
	print("Window: \t", window)

	# HISTOGRAMS
	plt.hist(image.ravel(), 256, [0,256])
	plt.savefig("../Images/originalImage_Histogram.png")

	for x in range(height - window):
		for y in range(width - window):
			newImage[x: x + window, y: y + window] = HistogramEqualization(image[x: x + window, y: y + window])

	plt.hist(newImage.ravel(), 256, [0,256])
	plt.savefig("../Images/localEqualization_Histogram(sliding).png")
	cv2.imwrite("../Images/localEqualization_Image(sliding).png", newImage)

def main():
	IMAGE_PATH = "../Images/img_lab08.png"
	image = cv2.imread(IMAGE_PATH, 0)
	window = 64

	# TilingApproach(image)
	SlidingWindowApproach(image.copy(), window)

if __name__ == '__main__':
	main()