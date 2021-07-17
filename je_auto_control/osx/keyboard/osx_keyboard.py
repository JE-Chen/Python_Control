import Quartz
import time

from je_auto_control.osx.core.osx_vk import key_shift

special_key = {
    "key_sound_up" : 0,
    "key_sound_down" : 1,
    "key_brightness_up": 2,
    "key_brightness_down":3,
    "key_capslock":4,
    "key_help":5,
    "key_power":6,
    "key_mute":7,
    "key_arrow_up":8,
    "key_arrow_down":9,
    "key_numlock":10,
    "key_contrast_up":11,
    "key_contrast_down":12,
    "key_launch_panel":13,
    "key_eject":14,
    "key_vidmirror":15,
    "key_play":16,
    "key_next":17,
    "key_previous":18,
    "key_fast":19,
    "key_rewind":20,
    "key_illumination_up": 21,
    "key_illumination_down": 22,
    "key_illumination_toggle": 23,
}


def normal_key(key, is_shift):
    if is_shift:
        event = Quartz.CGEventCreateKeyboardEvent(
            None,
            key_shift,
            True
        )
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        time.sleep(.001)
    event = Quartz.CGEventCreateKeyboardEvent(
        None,
        key,
        True
    )
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
    time.sleep(.001)


def special_key(key, is_shift):
    pass


def press_key(key):
    if key in special_key:
        pass
    else:
        pass


def release_key(key):
    if key in special_key:
        pass
    else:
        pass
