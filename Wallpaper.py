import ctypes
from random import choice
import os
try:
    basic_path = os.chdir(os.getcwd()+"\\Wallpaper\\")
    list_of_wallpapers = os.listdir()
    ran_pic = choice(list_of_wallpapers)
    ran_pic_path = os.getcwd()+"\\"+ran_pic
    if ctypes.windll.user32.SystemParametersInfoW(20, 0, ran_pic_path , 0):
        print("Wallpaper changed")
    else:
        print("Error while changing the wallpaper")
except Exception as e:
    print(e)
