import cv2, glob, os
import numpy as np

IMAGES_PATH = "../lab3 Images"
thresholds = [40, 70, 100, 200]

def Binarization(path):
	directory = "/".join(path.split('/')[:-1])
	extension = path.split('/')[-1].split('.')[1]
	file_name = path.split('/')[-1].split('.')[0]
	image = cv2.imread(path, 0)

	cv2.imshow("RGB Image", image)
	if not os.path.exists(directory + "/Binarized/"):
		os.makedirs(directory + "/Binarized/")

	for threshold in thresholds:
		binarized_img = np.where(image > threshold, 255, 0)
		# cv2.imshow("Binarized_" + file_name + "_" + str(threshold), binarized_img)
		cv2.imwrite(directory + "/Binarized/" + "Binarized_" + file_name + "_" + str(threshold) + "." + extension, binarized_img)
	cv2.waitKey(0)

def main():
	for file_name in glob.glob(IMAGES_PATH + "/*.*"):
		Binarization(file_name)

if __name__ == '__main__':
	main()