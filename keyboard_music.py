import sounddevice as sd
import numpy as np
import time
import ctypes

user32 = ctypes.WinDLL("user32")

WM_APPCOMMAND = 0x319
APPCOMMAND_KBD_BRIGHTNESS_UP = 0x00000016
HWND_BROADCAST = 0xffff

current_level = 0
max_level = 3

def brightness_up():
    user32.SendMessageW(HWND_BROADCAST, WM_APPCOMMAND, 0,
                        APPCOMMAND_KBD_BRIGHTNESS_UP << 16)

def set_level(target):
    global current_level

    diff = (target - current_level) % (max_level + 1)

    for _ in range(diff):
        brightness_up()
        time.sleep(0.05)

    current_level = target

def audio_callback(indata, frames, time_info, status):

    volume = np.linalg.norm(indata) * 10

    if volume < 2:
        set_level(0)

    elif volume < 5:
        set_level(1)

    elif volume < 10:
        set_level(2)

    else:
        set_level(3)

with sd.InputStream(callback=audio_callback):
    print("Listening for music... Press Ctrl+C to stop")

    while True:
        time.sleep(0.1)