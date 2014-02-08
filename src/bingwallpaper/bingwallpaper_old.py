import re
import urllib.request
import json
import xml.etree.cElementTree as ET

class BingWallpaperPage:
    BASE_URL = 'http://www.bing.com'
    IMAGE_API = '/HPImageArchive.aspx?format=js&idx={idx}&n={n}' #idx是起始日,n是天数.
    def __init__ (self, idx=0, n=2, base = BASE_URL, api = IMAGE_API, country_code = None):
        self.update(idx, n, base, api, country_code)

    def update(self, idx, n=10, base=BASE_URL, api=IMAGE_API, country_code=None):
        self.base = base
        self.api = api
        self.url = self.base + self.api.format(idx=idx, n=n)
        self.country_code = country_code
        if country_code:
            self.url = '&'.join([self.url, 'cc={}'.format(country_code)])
        self.content = urllib.request.urlopen(self.url).read().decode('utf-8')
        #self.content2 = self.content[1:-1]
        #self.json_string = json.dumps(self.content)
        self.data = json.loads(self.content)
        self.result = self.data['images']
        total = len(self.result)
        self.day1 = self.result[0]
        self.result_list = {%d,%d,%d}



bingwallpaper = BingWallpaperPage()
#print (bingwallpaper.content)
#print (bingwallpaper.json_string)
#print (bingwallpaper.data)
#print (bingwallpaper.url)
#print (type(bingwallpaper.json_string))
#print (type(bingwallpaper.data))
#print (bingwallpaper.result)
print (bingwallpaper.day1)


