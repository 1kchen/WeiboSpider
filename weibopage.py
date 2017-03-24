'''
init a weibo id page
'''

import requests
from html.parser import HTMLParser
import os

pics = []

class WeiboPage():
    name = ''
    uid = ''
    def __init__(self, name):
        self.name = name

    def getUserID(self):
        url = 'http://weibo.wbdacdn.com/search/user/?q={}&type=user&sa=%E6%89%BE%E5%91%80%E6%89%BE%E5%91%80'.format(self.name)
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; yie11; rv:11.0) like Gecko'}
        r = requests.get(url, headers = headers)
        url = r.url
        try:
            (int)(url.split(sep = '/')[-2])
        except ValueError:
            print("Cannot find this name.")
            return
        self.uid = url.split(sep = '/')[-2]
        print("UserID " + self.uid)
        return


    def getUserRss(self):
        url = 'http://rss.weibodangan.com/weibo/rss/{}/'.format((str)(self.uid))
        headers = {'user-agent': 'Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)'}
        r = requests.get(url, headers = headers)
        p = DeclHTMLParser()
        p.feed(r.text)

    def downloads(self):
        i = 0
        for each in pics:
            cmd = "wget " + "-P ~/pics/" + self.name + "/ " + each
            os.system(cmd)
            i += 1
        print("成功下载" + str(i) + "张图片。")
        print('保存在"~/pics/"。')

class DeclHTMLParser(HTMLParser):
    def unknown_decl(tag, decl):
        p = ImgHTMLParser()
        p.feed(decl)

class ImgHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == 'img') & (len(attrs) == 1):
            pics.append(attrs[-1][-1])
