import cv2
import os
import glob

folder = r"C:\Users\sambe\Downloads\ITA0513_CV"

images = []
for ext in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.JPG", "*.JPEG", "*.PNG"):
    images.extend(glob.glob(os.path.join(folder, ext)))

if images:
    image_path = images[0]
    print("Found image:", image_path)

    img = cv2.imread(image_path)

    if img is not None:
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image found, but OpenCV could not read it.")
else:
    print("No image found in the project folder!")
