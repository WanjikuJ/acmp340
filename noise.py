import matplotlib.pyplot as plt
from skimage import io, color, filters

# Load the image using scikit-image
input_image = io.imread('hero.jpg')

# Convert RGB to grayscale using scikit-image
grayscale_image_matplotlib = color.rgb2gray(input_image)

# Perform noise reduction using a Gaussian filter from scikit-image
smoothed_image_matplotlib = filters.gaussian(grayscale_image_matplotlib, sigma=10)

# Display the original and smoothed images using Matplotlib
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(input_image)
plt.title('Original Image')
plt.axis('off')
#hello world

# Grayscale image
plt.subplot(1, 3, 2)
plt.imshow(grayscale_image_matplotlib, cmap='gray')
plt.title('Grayscale Image')
plt.axis('on')

# Smoothed image
plt.subplot(1, 3, 3)
plt.imshow(smoothed_image_matplotlib)
plt.title('Smoothed Image')
plt.axis('off')

plt.tight_layout()
plt.show()
