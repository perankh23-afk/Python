import cv2
import matplotlib.pyplot as plt

image = cv2.imread('download.jpg')

image_rgh = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgh)
plt.title("RGB Image")
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

cropped_image = image[100:200, 200:400]
cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_image)
plt.title("Cropped Image")
plt.show()
