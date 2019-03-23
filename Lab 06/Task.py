import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

def unsharpEnhancement(image):
	unsharp_image = np.zeros(shape=image.shape)

	gaussian_3 = cv2.GaussianBlur(image, (9, 9), 10.0)
	# cv.AddWeighted(src1, alpha, src2, beta, gamma, dst)
	unsharp_image = cv2.addWeighted(image, 1.5, gaussian_3, -0.5, 0, image)
	return unsharp_image

def HistogramEqualization(image):
	equalizedImage = cv2.equalizeHist(image)
	return equalizedImage

def main():
	IMAGE_PATH = "Images/Landscape.jpg"
	image = cv2.imread(IMAGE_PATH, 0)
	figure(num=None, figsize=(20, 20), dpi=100, facecolor='w', edgecolor='k')

	# Histogram of Original Image
	plt.hist(image.ravel(), 256, [0,256])
	plt.show()

	unsharp_image = unsharpEnhancement(image)
	cv2.imwrite("Images/Unsharped.jpg", unsharp_image)
	figure(num=None, figsize=(20, 20), dpi=100, facecolor='w', edgecolor='k')

	# Histogram of Unsharped Image
	plt.hist(unsharp_image.ravel(), 256, [0,256])
	plt.show()

	# Stacking Image Side-by-Side
	stackedImage = np.hstack((image, unsharp_image))
	figure(num=None, figsize=(20, 20), dpi=100, facecolor='w', edgecolor='k')
	plt.imshow(stackedImage, cmap="gray")
	plt.show()

	equalizedImage = HistogramEqualization(unsharp_image)
	cv2.imwrite("Images/Equalized.jpg", equalizedImage)

	# Histogram of Equalized Image
	figure(num=None, figsize=(20, 20), dpi=100, facecolor='w', edgecolor='k')
	plt.hist(equalizedImage.ravel(), 256, [0,256])
	plt.show()

	# Stacking Image Side-by-Side (unsharped & Equalized)
	stackedImage = np.hstack((unsharp_image, equalizedImage))
	figure(num=None, figsize=(20, 20), dpi=100, facecolor='w', edgecolor='k')
	plt.imshow(stackedImage, cmap="gray")
	plt.show()

if __name__ == '__main__':
	main()