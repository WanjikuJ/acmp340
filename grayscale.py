import matplotlib.pyplot as plt
from skimage import io, color, filters

# Load the image using scikit-image
input_image = io.imread('hero.jpg')

# Convert RGB to grayscale using scikit-image
grayscale_image_matplotlib = color.rgb2gray(input_image)

# Display the original and smoothed images using Matplotlib
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(input_image)
plt.title('Original Image')
plt.axis('off')

# Grayscale image
plt.subplot(1, 2, 2)
plt.imshow(grayscale_image_matplotlib, cmap='gray')
plt.title('Grayscale Image')
plt.axis('on')


plt.tight_layout()
plt.show()
