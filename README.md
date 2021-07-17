# je_auto_control

## install
```
pip install je_auto_control
```

####

## example 

* All test in test dir

## Windows

#### mouse

```python
import time

from je_auto_control import win32_ctype_mouse_control as mouse_control
from je_auto_control.windows.mouse import win32_mouse_left
from je_auto_control.windows.mouse import win32_mouse_right

time.sleep(1)
print(mouse_control.position())
mouse_control.set_position(809, 388)
mouse_control.press_mouse(win32_mouse_right)
mouse_control.release_mouse(win32_mouse_right)
mouse_control.press_mouse(win32_mouse_left)
mouse_control.release_mouse(win32_mouse_left)

mouse_control.click_mouse(win32_mouse_left)
```

#### keyboard

```python
from je_auto_control import win32_keyT
from je_auto_control import win32_keyE
from je_auto_control import win32_keyS
from je_auto_control import win32_ctype_keyboard_control as keyboard_control

keyboard_control.press_key(win32_keyT)
keyboard_control.press_key(win32_keyE)
keyboard_control.press_key(win32_keyS)
keyboard_control.press_key(win32_keyT)

```

#### screen

```python
from je_auto_control import win32_screen

print(win32_screen.size())
```

#### scroll

```python
import time

from je_auto_control import win32_ctype_mouse_control as mouse_control

time.sleep(3)
print(mouse_control.position())
mouse_control.scroll(500)
```

#### Image detect one image

```python
import cv2

from je_auto_control import template_detection

# detect_threshold 0~1 , 1 is absolute equal
image_data_array = template_detection.find_image("../../test_template.png", detect_threshold=1, draw_image=True)

print(image_data_array[1])
print(image_data_array[2])

if len(image_data_array[2]) > 0:
    print("left_top", image_data_array[2][0], image_data_array[2][1])
    print("right_bottom", image_data_array[2][2], image_data_array[2][3])
    height = image_data_array[2][2] - image_data_array[2][0]
    width = image_data_array[2][3] - image_data_array[2][1]
    print(height, width)
    center = [int(height / 2), int(width / 2)]
    print(center)
    template_center = [image_data_array[2][0] + center[0], image_data_array[2][1] + center[1]]
    print(template_center)

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

```

#### Image detect multi image
```python
import cv2

from je_auto_control import template_detection

# detect_threshold 0~1 , 1 is absolute equal
image_data_array = template_detection.find_image_multi("../../test1.png", detect_threshold=1, draw_image=True)

print(image_data_array[1])

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

```
## Linux

#### mouse

```python
from je_auto_control import x11_linux_mouse_control as linux_mouse
from je_auto_control import x11_linux_mouse_right

print(linux_mouse.position())
linux_mouse.set_position(100, 100)
print(linux_mouse.position())
linux_mouse.click_mouse(x11_linux_mouse_right)


```

#### keyboard

```python
import time
from je_auto_control import x11_linux_keyboard_control as linux_keyboard
from je_auto_control import x11_linux_key_t
from je_auto_control import x11_linux_key_e
from je_auto_control import x11_linux_key_s

linux_keyboard.press_key(x11_linux_key_t)
linux_keyboard.release_key(x11_linux_key_t)
time.sleep(.01)
linux_keyboard.press_key(x11_linux_key_e)
linux_keyboard.release_key(x11_linux_key_e)
time.sleep(.01)
linux_keyboard.press_key(x11_linux_key_s)
linux_keyboard.release_key(x11_linux_key_s)
time.sleep(.01)
linux_keyboard.press_key(x11_linux_key_t)
linux_keyboard.release_key(x11_linux_key_t)

```

#### screen

```python
from je_auto_control import x11_linux_screen

print(x11_linux_screen.size())

```

#### scroll

```python
import time

from je_auto_control import x11_linux_mouse_control as linux_mouse

from je_auto_control import x11_linux_scroll_direction_down
from je_auto_control import x11_linux_scroll_direction_up

linux_mouse.scroll(5, x11_linux_scroll_direction_down)
time.sleep(1)
"""
this block just scroll test use








































"""
linux_mouse.scroll(5, x11_linux_scroll_direction_up)

```

#### Image detect
```python
from je_auto_control import template_detection

image_data_array = template_detection.find_image("../../test_template.png", draw_image=True)

print(image_data_array[1])
print(image_data_array[2])

if len(image_data_array[2]) > 0:
    print("left_top", image_data_array[2][0], image_data_array[2][1])
    print("right_bottom", image_data_array[2][2], image_data_array[2][3])
    height = image_data_array[2][2] - image_data_array[2][0]
    width = image_data_array[2][3] - image_data_array[2][1]
    print(height, width)
    center = [int(height / 2), int(width / 2)]
    print(center)
    template_center = [image_data_array[2][0] + center[0], image_data_array[2][1] + center[1]]
    print(template_center)


```

#### Image detect multi image
```python
from je_auto_control import template_detection

image_data_array = template_detection.find_image_multi("../../test_template.png", draw_image=True)

print(image_data_array[1])


```

## OSX

#### mouse

```python
from je_auto_control import osx_mouse
from je_auto_control import osx_mouse_right


osx_mouse.click_mouse(500, 100, osx_mouse_right)
print(osx_mouse.position())

```

#### keyboard

```python
from je_auto_control import osx_keyboard
from je_auto_control import osx_key_t
from je_auto_control import osx_key_e
from je_auto_control import osx_key_s

osx_keyboard.press_key(osx_key_t, False)
osx_keyboard.press_key(osx_key_e, False)
osx_keyboard.press_key(osx_key_s, False)
osx_keyboard.press_key(osx_key_t, False)

```

#### screen

```python
from je_auto_control import osx_screen

print(osx_screen.size())

```

#### scroll

```python
from je_auto_control import osx_mouse

osx_mouse.scroll(100)

```

#### Image detect
```python
from je_auto_control import template_detection

image_data_array = template_detection.find_image_multi("../../test_template.png", draw_image=True)

print(image_data_array[1])


```

#### Image detect multi image
```python
from je_auto_control import template_detection

image_data_array = template_detection.find_image("../../test_template.png", draw_image=True)

print(image_data_array[1])
print(image_data_array[2])

if len(image_data_array[2]) > 0:
    print("left_top", image_data_array[2][0], image_data_array[2][1])
    print("right_bottom", image_data_array[2][2], image_data_array[2][3])
    height = image_data_array[2][2] - image_data_array[2][0]
    width = image_data_array[2][3] - image_data_array[2][1]
    print(height, width)
    center = [int(height / 2), int(width / 2)]
    print(center)
    template_center = [image_data_array[2][0] + center[0], image_data_array[2][1] + center[1]]
    print(template_center)


```
