import cv2, glob, os
import numpy as np
import matplotlib.pyplot as plt

IMAGES_PATH = "../lab3 Images"

def Histogram(image):
	gray_image = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2GRAY)
	image_array = np.array(gray_image)
	elements, counts = np.unique(image_array, return_counts = True)
	# print("Counts", counts)
	plt.bar(elements, counts)
	if not os.path.exists(IMAGES_PATH + "/Histograms/"):
		os.makedirs(IMAGES_PATH + "/Histograms/")

	plt.savefig(IMAGES_PATH + "/Histograms/Histogram_" + image.split('/')[-1].split('.')[0] + ".png", dpi = 100)
	plt.show()

def main():
	for file_name in glob.glob(IMAGES_PATH + "/*.*"):
		Histogram(file_name)

if __name__ == '__main__':
	main()