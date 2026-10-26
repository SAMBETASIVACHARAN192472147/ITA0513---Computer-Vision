
import cv2

img = cv2.imread(r"C:\Users\sambe\Downloads\ITA0513_CV\Head.jpg")

if img is None:
    print("Image not found!")
else:
    watermark = img.copy()

    cv2.putText(
        watermark, "MY WATERMARK",
        (30, img.shape[0] - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2, (255, 255, 255), 3
    )

    cv2.imshow("Watermarked Image", watermark)
    cv2.imwrite(
        r"C:\Users\sambe\Downloads\ITA0513_CV\watermarked.jpg",
        watermark
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Watermarked image saved!")
