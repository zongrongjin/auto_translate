import os
from random import choice

import pyautogui as pag
import win32api
import win32clipboard as wincld
import win32con
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from PIL import Image
from io import BytesIO


filepaths = []
def all_file(your_dir):
    for root, dirs, files in os.walk(your_dir):     # 分别代表根目录、文件夹、文件
        for file in files:                         # 遍历文件
            file_path = os.path.join(root, file)   # 获取文件绝对路径  
            filepaths.append(file_path)            # 将文件路径添加进列表
        for dir in dirs:                           # 遍历目录下的子目录
            dir_path = os.path.join(root, dir)     # 获取子目录路径
            all_file(dir_path)               # 递归调用

def set_text(strings):
    wincld.OpenClipboard()
    wincld.EmptyClipboard()
    wincld.SetClipboardData(win32con.CF_UNICODETEXT, strings)
    wincld.CloseClipboard()

def get_text():
    wincld.OpenClipboard()
    d = wincld.GetClipboardData(win32con.CF_TEXT)
    wincld.CloseClipboard()
    return(d).decode('GBK')

def get_mouse_position():
    x, y = pag.position()
    return x, y

def mouse_click(x, y):
    mouse = PyMouse()
    mouse.click(x, y)

def tap_enter():
    kb = PyKeyboard()
    kb.tap_key(kb.enter_key)

def send_text(msg):
    kb = PyKeyboard()
    kb.type_string(msg)

def ctrl_v():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,0,0,0)  #v键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

def ctrl_x():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(88,0,0,0)  #v键位码是86
    win32api.keybd_event(88,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

def ctrl_a():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(65,0,0,0)  #v键位码是86
    win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

    