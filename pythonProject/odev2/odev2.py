import cv2
import numpy as np

image_path = "inverter.jpeg"

image = cv2.imread(image_path)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

red_mask = cv2.inRange(hsv, lower_red, upper_red)

red_result = cv2.bitwise_and(image, image, mask=red_mask)

cv2.imshow("Red Object Detection", red_result)
cv2.waitKey(0)  # Herhangi bir tuşa basana kadar pencereyi açık tutun

cv2.destroyAllWindows()
