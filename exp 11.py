
import cv2

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imshow("180 Degree Rotation", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
