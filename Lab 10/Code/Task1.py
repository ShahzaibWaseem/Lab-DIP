import numpy as np
import cv2

def main():
	IMAGE_PATH = "../Images/"
	imageName = "Signature.png"
	image = cv2.imread(IMAGE_PATH + imageName, 0)

	# Inverse Binarization
	ret, inverseImage = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
	kernel = np.ones((5, 5), np.uint8)

	cv2.imwrite(IMAGE_PATH + "inv_" + imageName, inverseImage)
	cv2.imshow("Signature (Inverse)", inverseImage)
	cv2.waitKey(0)

	eroded = cv2.erode(inverseImage, kernel, iterations=1)
	cv2.imwrite(IMAGE_PATH + "eroded_" + imageName, eroded)
	cv2.imshow("Erosion", eroded)
	cv2.waitKey(0)

	dilated = cv2.dilate(inverseImage, kernel, iterations=1)
	cv2.imwrite(IMAGE_PATH + "dilated_" + imageName, dilated)
	cv2.imshow("Dilation", dilated)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()