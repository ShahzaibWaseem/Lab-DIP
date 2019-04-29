import cv2
import numpy as np

def main():
	IMAGE_PATH = "../Images/ThumbImpression.png"
	image = cv2.imread(IMAGE_PATH, 0)
	kernel = np.ones((2, 2), np.uint8)

	size = np.size(image)
	skeleton = np.zeros(image.shape, np.uint8)

	ret,image = cv2.threshold(image, 127, 255, 0)
	element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
	done = False

	while(not done):
	    eroded = cv2.erode(image, element)
	    temp = cv2.dilate(eroded, element)
	    temp = cv2.subtract(image, temp)
	    skeleton = cv2.bitwise_or(skeleton, temp)
	    image = eroded.copy()

	    zeros = size - cv2.countNonZero(image)
	    if zeros == size:
	        done = True

	cv2.imshow("Skeleton Image", skeleton)
	retval, image = cv2.threshold(skeleton, 0, 255, cv2.THRESH_BINARY_INV)

	eroded = cv2.erode(image, kernel, iterations=2)
	dilated = cv2.dilate(eroded, kernel, iterations=2)
	eroded = cv2.erode(dilated, kernel, iterations=2)

	image = cv2.medianBlur(eroded, 9)

	cv2.imwrite("../Images/" + IMAGE_PATH.split('/')[-1].split('.')[0] + "_out.png", image)
	cv2.imshow("Median Blur Image", image)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()