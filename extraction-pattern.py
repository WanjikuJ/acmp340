import matplotlib.pyplot as plt
from skimage import io, color, feature
import tkinter
# Load the image using scikit-image
input_image = io.imread('hero.jpg')

# Convert the image to grayscale
grayscale_image = color.rgb2gray(input_image)

# Extract Histogram of Oriented Gradients (HOG) features
hog_features, hog_image = feature.hog(
    grayscale_image, visualize=True, block_norm='L2-Hys', pixels_per_cell=(8, 8), cells_per_block=(1, 1))

# Display the original image and HOG features using Matplotlib
plt.figure(figsize=(12, 6))

# Original grayscale image
plt.subplot(1, 2, 1)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# HOG features
plt.subplot(1, 2, 2)
plt.imshow(hog_image, cmap='gray')
plt.title('HOG Features')
plt.axis('off')

plt.tight_layout()
plt.show()
