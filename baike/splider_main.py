# -*- coding: utf-8 -*-
# 入口程序
# import url_manager
# from url_manager import UrlManager
# from html_downloader import HtmlDownloader
# from html_outputer import HtmlOutputer
# from html_parser import HtmlParser

import url_manager 
import html_downloader 
import html_outputer 
import html_parser 

class SpiderMain(object):  
    def __init__(self):  
        self.urls = url_manager.UrlManager()  
        self.downloader = html_downloader.HtmlDownloader()  
        self.parser = html_parser.HtmlParser()  
        self.outputer = html_outputer.HtmlOutputer()  
  
    def craw(self):  
        count = 1  
        self.urls.add_new_url(root_url)  
        while self.urls.has_new_url():  
            try:  
                new_url = self.urls.get_new_url()  
                print('craw %d: %s' % (count, new_url))  
                html_cont = self.downloader.download(new_url)  
                new_urls, new_data = self.parser.parse(new_url, html_cont)  
                self.urls.add_new_urls(new_urls)  
                self.outputer.collect_data(new_data)  
  
                if count == 5:  
                    break  
                count += 1  
            except Exception as e:  
                print('craw failed')  
                print(e)  
  
        self.outputer.output_html()  
  
if __name__ == '__main__':  
    root_url = 'http://baike.so.com/doc/1790119-1892991.html'  
    obj_spider = SpiderMain()  
    obj_spider.craw()  