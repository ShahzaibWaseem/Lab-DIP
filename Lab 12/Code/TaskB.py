import cv2, math

"""
Task 1: Bounding Box
"""
def BoundingBox(image, height, width):
	left, right = width, 0
	top, bottom = height, 0

	for x in range(width):
		for y in range(height):
			color = image[y, x]
			if color == 0:
				if x > right:
					right = x
				if x < left:
					left = x
				if y > bottom:
					bottom = y
				if y < top:
					top = y

	return top, bottom, left, right

"""
Task 2: Finding Centroid
"""
def FindCentroid(image, left, right, top, bottom):
	cx, cy = 0, 0
	n = 0

	for x in range(left, right):
		for y in range(top, bottom):
			if image[y, x] == 0:
				cx = cx + x
				cy = cy + y
				n = n + 1
	if n == 0:
		return ((left + right) // 2, (top + bottom) // 2, n)
	else:
		return (cx // n, cy // n, n)

"""
Task 3: Dividing Centroid
"""
def DivideBoundingBox(centroid_image, top, bottom, left, right, cx, cy):
	segmented_image = cv2.rectangle(centroid_image, (left, top), (cx, cy), (0,255,0), 3)		# top left
	segmented_image = cv2.rectangle(segmented_image, (cx, top), (right, cy), (0,255,0), 3)		# bottom left
	segmented_image = cv2.rectangle(segmented_image, (left, cy), (cx, bottom), (0,255,0), 3)	# top right
	segmented_image = cv2.rectangle(segmented_image, (cx, cy), (right, bottom), (0,255,0), 3)	# bottom right

	top_left = centroid_image[top: cy, left: cx]
	bottom_left = centroid_image[top: cy, cx: right]
	top_right = centroid_image[cy: bottom, left: cx]
	bottom_right = centroid_image[cy: bottom, cx: right]

	return top_left, bottom_left, top_right, bottom_right, segmented_image

"""
Task 4: Black to White Transitions
"""
def B2W_Transitions(image):
	height, width = image.shape
	countB2W = 0

	if height == 0 or width == 0:
		return 0
	prevPixel = image[0, 0]

	for x in range(width):
		for y in range(height):
			currPixel = image[y, x]

			if (currPixel == 255) and (prevPixel == 0):
				countB2W += 1
			prevPixel = currPixel

	return countB2W

def main():
	IMAGE_PATH = "../Images/Signature.png"
	image = cv2.imread(IMAGE_PATH, 0)
	height, width = image.shape

	retval, binarized_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
	cv2.imwrite("../Images/" + IMAGE_PATH.split('/')[-1].split('.')[0] + "_binarized.png", binarized_image)
	cv2.imshow("Binarized Signature", binarized_image)

	top, bottom, left, right = BoundingBox(binarized_image, height, width)
	bounding_box_image = cv2.rectangle(binarized_image, (left, top), (right, bottom), (0,255,0), 3)
	cv2.imwrite("../Images/" + IMAGE_PATH.split('/')[-1].split('.')[0] + "_box.png", bounding_box_image)
	cv2.imshow("Bounding Box Image", bounding_box_image)
	B = (left, right, top, bottom)

	cx, cy, n = FindCentroid(bounding_box_image, left, right, top, bottom)
	centroid_image = cv2.circle(bounding_box_image, (int(cy), int(cx)), 10, 200, -1)
	cv2.imwrite("../Images/" + IMAGE_PATH.split('/')[-1].split('.')[0] + "_centroid.png", centroid_image)
	cv2.imshow("Centroid Image", centroid_image)
	C = (cx, cy)

	top_left, bottom_left, top_right, bottom_right, segmented_image = DivideBoundingBox(centroid_image, top, bottom, left, right, cy, cx)
	cv2.imwrite("../Images/" + IMAGE_PATH.split('/')[-1].split('.')[0] + "_segmented.png", segmented_image)
	cv2.imshow("Divided Image", segmented_image)

	cv2.imshow("top_left", top_left)
	cv2.imshow("bottom_left", bottom_left)
	cv2.imshow("top_right", top_right)
	cv2.imshow("bottom_right", bottom_right)

	# Task 4
	TL = B2W_Transitions(top_left)
	BL = B2W_Transitions(bottom_left)
	TR = B2W_Transitions(top_right)
	BR = B2W_Transitions(bottom_right)
	T = (TL, TR, BL, BR)

	print("Bounding Box\t:\t", B)
	print("Centroid\t:\t", C)
	print("Transitions\t:\t", T)

	cv2.waitKey(0)

if __name__ == '__main__':
	main()