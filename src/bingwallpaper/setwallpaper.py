# -*- coding: UTF-8 -*-

import os
import PIL.Image
import urllib.request
import win32gui
import win32con
import win32api
import bingwallpaper

image_name = bingwallpaper.image_name()
home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
STORE_FOLDER = os.path.join(home, 'BingWallpaper\\')


def set_wallpaper_from_bmp(image_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")  # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1+2)


def set_wallpaper(image_path):
    """获得一个图片路径，并变成BMP保存到STORE_FOLDER文件夹"""
    if os.path.exists(STORE_FOLDER):
        pass
    else:
        os.mkdir(STORE_FOLDER)

    if os.listdir(STORE_FOLDER):
        file_list = os.listdir(STORE_FOLDER)
        for file_name in file_list:
            if file_name != image_name.replace('.jpg', '.bmp'):
                os.remove(STORE_FOLDER + file_name)
                bmp_image = PIL.Image.open(image_path)
                new_path = STORE_FOLDER + image_name.replace('.jpg', '.bmp')
                bmp_image.save(new_path, "BMP")
            else:
                new_path = STORE_FOLDER + file_name
    else:
        bmp_image = PIL.Image.open(image_path)
        new_path = STORE_FOLDER + image_name.replace('.jpg', '.bmp')
        bmp_image.save(new_path, "BMP")

    set_wallpaper_from_bmp(new_path)


def get_image():
    image_path = 'BingWallpaper\\' + image_name

    #保存到文件夹下，如果文件夹存在就跳过，如果不存在就新建文件夹
    if os.path.exists('BingWallpaper\\'):
        pass
    else:
        os.mkdir('BingWallpaper\\')

    with open(image_path, 'wb') as a_file:
        a_file.write(urllib.request.urlopen(bingwallpaper.image_url()).read())

    set_wallpaper(image_path)

get_image()