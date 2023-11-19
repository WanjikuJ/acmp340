import matplotlib.pyplot as plt
from skimage import io, color, filters
from skimage.filters import threshold_otsu

# Load the image using scikit-image
input_image = io.imread('demo.jpeg')

# Convert RGB to grayscale using scikit-image
grayscale_image = color.rgb2gray(input_image)

# Perform noise reduction using a Gaussian filter
smoothed_image = filters.gaussian(grayscale_image, sigma=1)

# Thresholding using Otsu's method
threshold_value = threshold_otsu(smoothed_image)
binary_image = smoothed_image > threshold_value

# Display the original and binary images using Matplotlib
plt.figure(figsize=(8, 4))

# Original grayscale image
plt.subplot(1, 2, 1)
plt.imshow(smoothed_image, cmap='gray')
plt.title('Smoothed Image')
plt.axis('off')

# Binary segmented image after thresholding
plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap='binary')
plt.title('Binary Image (Thresholded)')
plt.axis('off')

plt.tight_layout()
plt.show()

