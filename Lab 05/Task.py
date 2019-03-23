import cv2
import numpy as np
import matplotlib.pyplot as plt

# Accepts NumPy Array
def NegativeImage(image, height, width):
	for row in range(height):
		for column in range(width):
			red = 255 - image[row][column][0]
			green = 255 - image[row][column][1]
			blue = 255 - image[row][column][2]
			image[row, column] = [red, green, blue]
	return image

def Binarization(image, filename):
	retval, binarized_img = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
	cv2.imwrite(filename, binarized_img)
	return binarized_img

def HorizontalDerivative(image, height, width):
	image_gradient = np.zeros((height, width), dtype = np.uint8)
	for row in range(height - 1):
		for column in range(width - 1):
			try:
				image_gradient[row, column] = image[row + 1, column] - image[row, column]
			except Exception as e:
				pass
	return image_gradient

def BitPlaneSlicing(image, plane):
	image[np.bitwise_and(image, 2**plane) == 0] = 0
	image[np.bitwise_and(image, 2**plane) != 0] = 255
	return image

def main():
	IMAGE_PATH = "./Files/lenna.png"
	directory = "/".join(IMAGE_PATH.split('/')[:-1])
	extension = IMAGE_PATH.split('/')[-1].split('.')[1]
	file_name = IMAGE_PATH.split('/')[-1].split('.')[0]

	# Opening Image
	image = cv2.imread(IMAGE_PATH)
	height, width, channels = image.shape

	cv2.imshow("Lenna", image)

	negative = NegativeImage(image, height, width)
	cv2.imwrite("Files/Negative.png", negative)
	cv2.imshow("Negative Fruits", negative)

	image = cv2.imread(IMAGE_PATH, 0)
	binarized_img = Binarization(image, "Files/binarized_img.png")

	hD = HorizontalDerivative(binarized_img, height, width)
	cv2.imwrite("Files/HorizontalDerivative.png", hD)
	cv2.imshow("Horizontal Derivative", hD)

	image = cv2.imread(IMAGE_PATH, 0)
	for plane in range(0, 8):
		bpSlicing = BitPlaneSlicing(image.copy(), plane)
		cv2.imwrite("Files/BitPlane_" + str(plane) + "." + extension, bpSlicing)
		cv2.imshow("Bit Plane Slicing" + str(plane), bpSlicing)

	cv2.waitKey(0)

if __name__ == '__main__':
	main()