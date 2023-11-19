import matplotlib.pyplot as plt
from skimage import io, color, morphology
from skimage.filters import threshold_otsu

# Load the image using scikit-image
input_image = io.imread('demo.jpeg')

# Convert the image to grayscale
grayscale_image = color.rgb2gray(input_image)

# Thresholding using Otsu's method
threshold_value = threshold_otsu(grayscale_image)
binary_image = grayscale_image > threshold_value

# Perform morphological dilation and erosion
dilated_image = morphology.dilation(binary_image, morphology.disk(5))
eroded_image = morphology.erosion(dilated_image, morphology.disk(5))

# Display the original, binary, dilated, and eroded images using Matplotlib
plt.figure(figsize=(12, 4))

# Original grayscale image
plt.subplot(1, 4, 1)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Binary segmented image after thresholding
plt.subplot(1, 4, 2)
plt.imshow(binary_image, cmap='binary')
plt.title('Binary Image (Thresholded)')
plt.axis('off')

# Dilated image
plt.subplot(1, 4, 3)
plt.imshow(dilated_image, cmap='binary')
plt.title('Dilated Image')
plt.axis('off')

# Eroded image
plt.subplot(1, 4, 4)
plt.imshow(eroded_image, cmap='binary')
plt.title('Eroded Image')
plt.axis('off')

plt.tight_layout()
plt.show()
