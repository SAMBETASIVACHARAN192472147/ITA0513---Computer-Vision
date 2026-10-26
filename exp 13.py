
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    h, w = img.shape[:2]

    src = np.float32([
        [0, 0], [w - 1, 0], [0, h - 1]
    ])

    dst = np.float32([
        [50, 50], [w - 100, 0], [100, h - 50]
    ])

    matrix = cv2.getAffineTransform(src, dst)
    result = cv2.warpAffine(img, matrix, (w, h))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("Affine Transformation")
    plt.axis("off")

    plt.show()
