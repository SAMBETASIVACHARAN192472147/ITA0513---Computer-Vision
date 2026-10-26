
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(path):
    img = cv2.imread(path)

    if img is None:
        print("Image not found!")
        return

    colors = ("b", "g", "r")
    labels = ("Blue", "Green", "Red")

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=labels[i])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Pixel Count")
    plt.legend()
    plt.show()

analyze_histogram(
    r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg"
)
