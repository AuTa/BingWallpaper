# -*- coding: UTF-8 -*-

import urllib.request
import json

BASE_URL = 'http://www.bing.com'
url_json = urllib.request.urlopen(BASE_URL + '/HPImageArchive.aspx?format=js&idx=0&n=1&cc=cn')
content = url_json.read().decode('utf-8')
data = json.loads(content)
images = data['images']
urlbase = images[0]['urlbase']
enddate = images[0]['enddate']
url = BASE_URL + urlbase + '_1920x1080.jpg'


#下载的图片名称
def image_name():
    if images[0]['msg']:
        text = images[0]['msg'][0]['text']
    else:
        text = urlbase.split('/')[4].split('_')[0]
    _image_name = '_'.join([enddate, text]) + '.jpg'
    return _image_name


#图片URL
def image_url():
    _image_url = BASE_URL + ''.join([urlbase + '_1920x1080.jpg'])
    return _image_url