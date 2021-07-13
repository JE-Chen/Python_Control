from PIL import ImageGrab
from je_open_cv import template_detection


def find_image(image, draw_image=False):
    grab_image = ImageGrab.grab()
    return template_detection.find_object_cv2_with_pil(grab_image, image, draw_image=draw_image)


def find_image_multi(image, draw_image=False):
    grab_image = ImageGrab.grab()
    return template_detection.find_multi_object_cv2_with_pil(grab_image, image, draw_image=draw_image)
