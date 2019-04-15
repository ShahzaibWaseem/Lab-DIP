import numpy as np
import cv2

def main():
	IMAGE_PATH = "../Images/"
	imageName = "UrduSignature.jpg"
	image = cv2.imread(IMAGE_PATH + imageName, 0)
	kernel = np.ones((3, 3), np.uint8)

	ret, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
	ret, inverseImage = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

	cv2.imwrite(IMAGE_PATH + "inv_" + imageName, inverseImage)
	cv2.imshow("Signature (Inverse)", inverseImage)
	cv2.waitKey(0)

	eroded = cv2.erode(inverseImage, kernel, iterations=1)
	dilated = cv2.dilate(eroded, kernel, iterations=2)
	cv2.imwrite(IMAGE_PATH + "processed_" + imageName, dilated)
	cv2.imshow("Processed Image", dilated)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()