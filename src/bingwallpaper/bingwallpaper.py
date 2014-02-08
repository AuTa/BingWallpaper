import urllib.request
import json
import os

BASE_URL = 'http://www.bing.com'
url_json = urllib.request.urlopen(BASE_URL + '/HPImageArchive.aspx?format=js&idx=0&n=1&cc=us')
content = url_json.read().decode('utf-8')
data = json.loads(content)

images = data['images']
urlbase = images[0]['urlbase']
enddate = images[0]['enddate']
if images[0]['msg']:
    text = images[0]['msg'][0]['text']
else:
    text = urlbase.split('/')[4].split('_')[0]
url = BASE_URL + urlbase + '_1920x1080.jpg'

#保存到文件夹下，如果文件夹存在就跳过，如果不存在就新建文件夹
if os.path.exists('BingWallpaper\\'):
    pass
else:
    os.mkdir('BingWallpaper\\')

with open('BingWallpaper\\' + enddate + '_' + text + '.jpg', 'wb') as a_file:
    a_file.write(urllib.request.urlopen(url).read())
