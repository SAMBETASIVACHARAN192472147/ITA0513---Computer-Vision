
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    edge_x = cv2.convertScaleAbs(sx)
    edge_y = cv2.convertScaleAbs(sy)

    combined = cv2.addWeighted(edge_x, 0.5, edge_y, 0.5, 0)

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(combined, cmap="gray")
    plt.title("Sobel Edges")
    plt.axis("off")

    plt.show()
