# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AppstorePipeline(object):
	def __init__(self):
		#self.file = open('appstore.dat', 'wb')
		#self.re_file = open('appstore_re.dat', 'wb')
		self.file = open('items.json', 'w')

	def process_item(self, item, spider):
		#val = "{0}\t{1}\t{2}\n".format(item['appid'], item['title'], item['intro'])
		#self.file.write(val)
		#val2 = "{0}\t{1}\t{2}\t{3}\n".format(item['appid'], item['url'], item['title'], item['recommended'])
		#self.re_file.write(val2)
		line = json.dumps(dict(item),ensure_ascii=False) + "\n"
		self.file.write(line)
		return item
