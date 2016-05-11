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

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			# try:
				new_url = self.urls.get_new_url()

				print 'craw %d : %s' % (count, new_url)

				html_cont = self.downloader.download(new_url)
				new_urls, new_data = self.parser.parse(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)

				if count == 10:
					break

				count = count + 1
			# except :
			# 	print "craw failed"

		self.outputer.output_html()

if __name__=="__main__":
	# 入口url、
	root_url = 'http://baike.baidu.com/view/21087.htm'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)