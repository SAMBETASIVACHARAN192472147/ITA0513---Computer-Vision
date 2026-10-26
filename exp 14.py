
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    h, w = img.shape[:2]

    src = np.float32([
        [0, 0], [w - 1, 0],
        [0, h - 1], [w - 1, h - 1]
    ])

    dst = np.float32([
        [50, 50], [w - 100, 0],
        [0, h - 50], [w - 50, h - 100]
    ])

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (w, h))

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
