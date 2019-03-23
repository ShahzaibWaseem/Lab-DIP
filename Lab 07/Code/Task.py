import cv2
import matplotlib.pyplot as plt
import numpy as np

def HistogramEqualization(image):
	height, width = image.shape
	N = height*width
	image_pixel = np.zeros(image.shape)
	newImage = np.zeros(image.shape)

	print("Size: ", height, width)

	for x in range(height):
		for y in range(width):
			image_pixel[image[x,y]] += 1

	image_pixel, values = np.histogram(image.flatten(), 256, [0, 256])
	prob_dist = np.ceil(((256 - 1) * image_pixel) / image.size)
	cumm_dist = prob_dist.cumsum()

	for x in range(height):
		for y in range(width):
			newImage[x,y] = cumm_dist[image[x,y]]

	cv2.imwrite("../Images/newImage.png", newImage)
	plt.hist(newImage.ravel(), 256, [0,256])
	plt.savefig("../Images/newImage_Histogram.png")
	plt.show()

def main():
	IMAGE_PATH = "../Images/hist2.tif"
	image = cv2.imread(IMAGE_PATH, 0)
	cv2.imwrite("../Images/originalImage.png", image)

	# Histogram of Original Image
	plt.hist(image.ravel(), 256, [0,256])
	plt.savefig("../Images/originalImage_Histogram.png")
	# plt.show()

	HistogramEqualization(image)


if __name__ == '__main__':
	main()