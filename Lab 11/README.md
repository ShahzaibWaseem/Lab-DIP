# Lab 11: Image Segmentation

## Task

1. Read input image (RGB).
2. Use thresholding (Otsu’s method) to segment foreground from background.
3. Clean the binary image using appropriate morphological operations.
4. Label the objects using different color values like, red, green, blue, etc. (yes, the image will be converted back to RGB). You might need bounding box and connected component analysis.
5. Ask the user to select some color out of those available in the processed image.
6. Count the objects with the specified color.