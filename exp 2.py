
import cv2
import matplotlib.pyplot as plt

# Read the image
image_path = r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found! Check the path.")
else:
    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display images
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(blur)
    plt.title("Gaussian Blur")
    plt.axis("off")

    plt.show()
