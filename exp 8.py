
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )
    dilated = cv2.dilate(binary, kernel, iterations=1)

    plt.subplot(1, 2, 1)
    plt.imshow(binary, cmap="gray")
    plt.title("Original Binary")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(dilated, cmap="gray")
    plt.title("Dilated Image")
    plt.axis("off")

    plt.show()
