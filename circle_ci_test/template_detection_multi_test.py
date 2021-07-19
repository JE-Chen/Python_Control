import cv2

from je_auto_control import template_detection

# detect_threshold 0~1 , 1 is absolute equal
image_data_array = template_detection.find_image_multi("test1.png", detect_threshold=1, draw_image=True)

print(image_data_array[1])

