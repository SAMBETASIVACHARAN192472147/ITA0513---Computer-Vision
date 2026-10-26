
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    bigger = cv2.resize(
        img, None, fx=1.5, fy=1.5,
        interpolation=cv2.INTER_LINEAR
    )

    smaller = cv2.resize(
        img, None, fx=0.5, fy=0.5,
        interpolation=cv2.INTER_AREA
    )

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))
    plt.title("Bigger")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
    plt.title("Smaller")
    plt.axis("off")

    plt.show()
