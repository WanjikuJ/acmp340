
# Import the necessary Libraries 
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import tkinter
  
# Load the image 
image = cv2.imread('hero.jpg') 
  
# Convert BGR image to RGB 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
  
cv2.imshow('Original Image', image) 
cv2.waitKey(0) 

# Apply Gaussian blur 
blurred = cv2.GaussianBlur(image, (7, 7), 0) 
cv2.imshow('Gaussian Blurring', Gaussian) 
cv2.waitKey(0) 

cv2.destroyAllWindows() 
# Convert blurred image to RGB 
# blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB) 
  
# # Create subplots 
# fig, axs = plt.subplots(1, 2, figsize=(7, 4)) 
  
# # Plot the original image 
# axs[0].imshow(image_rgb) 
# axs[0].set_title('Original Image') 
  
# # Plot the blurred image 
# axs[1].imshow(blurred_rgb) 
# axs[1].set_title('Blurred Image') 
  
# # Remove ticks from the subplots 
# for ax in axs: 
#     ax.set_xticks([]) 
#     ax.set_yticks([]) 
  
# # Display the subplots 
# plt.tight_layout() 
# plt.show()