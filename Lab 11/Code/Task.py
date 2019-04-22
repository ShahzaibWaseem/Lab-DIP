import cv2
import numpy as np

def main():
	IMAGE_PATH = "../Images/Fruits.png"
	image = cv2.imread(IMAGE_PATH, 0)
	kernel = np.ones((2, 2), np.uint8)

	retval, binarizedImage = cv2.threshold(image, 40, 255, cv2.THRESH_BINARY)
	retval, binarizedImage = cv2.threshold(binarizedImage, 40, 255, cv2.THRESH_OTSU)

	dilated = cv2.dilate(binarizedImage, kernel, iterations=2)
	eroded = cv2.erode(dilated, kernel, iterations=6)
	retval, labels = cv2.connectedComponents(eroded)

	cv2.imshow("Image", image)
	cv2.imshow("Binarized then Dilated((2, 2), 4) then Eroded((2, 2), 6) Image", eroded)
	cv2.imshow("Applying Connected Component Labeling", retval)
	cv2.imwrite("../Images/Fruits_out.png", eroded)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()