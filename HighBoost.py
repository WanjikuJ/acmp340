import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('demo.jpeg')

# Apply Gaussian blur to the image
blurred = cv2.GaussianBlur(image, (0, 0), 3)

# Calculate the high-boost filtered image
k = 1.5  # Boosting factor (adjust as needed)
highboost = cv2.addWeighted(image, 1 + k, blurred, -k, 0)

# Display the original and high-boost filtered images using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(highboost, cv2.COLOR_BGR2RGB))
plt.title('High-Boost Filtered Image')
plt.axis('off')

plt.show()
