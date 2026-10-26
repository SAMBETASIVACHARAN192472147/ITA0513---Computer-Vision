
import cv2

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    h, w = img.shape[:2]

    # Crop a central region
    x, y = w // 4, h // 4
    roi = img[y:y + h // 2, x:x + w // 2].copy()

    # Paste ROI at the top-left corner
    rh, rw = roi.shape[:2]
    img[0:rh, 0:rw] = roi

    cv2.imshow("Cropped Region", roi)
    cv2.imshow("Image After Copy and Paste", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
