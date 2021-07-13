import time

import cv2

from je_auto_control import template_detection

image_data_array = template_detection.find_image_multi("../../test_template.png", draw_image=True)

print(image_data_array[1])

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
