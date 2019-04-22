import cv2
import numpy as np

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0
    return labeled_img

def main():
	IMAGE_PATH = "../Images/Fruits.png"
	image = cv2.imread(IMAGE_PATH, 0)
	kernel = np.ones((2, 2), np.uint8)

	retval, binarizedImage = cv2.threshold(image, 40, 255, cv2.THRESH_BINARY)
	retval, binarizedImage = cv2.threshold(binarizedImage, 40, 255, cv2.THRESH_OTSU)

	dilated = cv2.dilate(binarizedImage, kernel, iterations=2)
	eroded = cv2.erode(dilated, kernel, iterations=6)
	retval, labels = cv2.connectedComponents(eroded)
	ccl_Image = imshow_components(labels)

	cv2.imshow("Image", image)
	cv2.imshow("Binarized then Dilated((2, 2), 4) then Eroded((2, 2), 6) Image", eroded)
	cv2.imshow("Applying Connected Component Labeling", ccl_Image)

	cv2.imwrite("../Images/Fruits_out.png", eroded)
	cv2.imwrite("../Images/Fruits_ccl.png", ccl_Image)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()