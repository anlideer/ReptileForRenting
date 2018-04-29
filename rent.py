#!usr/bin/env python3
#-*- coding: utf-8 -*-

# 学院路 五道口 二里庄 南沙滩 健翔桥 牡丹园 马甸 北太平庄 知春路 
# 双榆树 皂君庙 中关村 知春里 西土城 大钟寺 健德门  

import requests, re, os
from bs4 import BeautifulSoup
import datetime

# 在这里自定义搜索范围（作为关键字）
areas = ['学院路', '五道口', '二里庄', '南沙滩', '健翔桥', '牡丹园', '马甸', '北太平庄',
'知春路', '双榆树', '皂君庙', '中关村', '知春里', '西土城', '大钟寺', '健德门']
os.chdir('D://Workplace/rent')	# 当前目录...
date = datetime.datetime.now()
f = open(str(date.year) + str(date.month) + str(date.day) + '.txt', 'w', encoding='utf-8')

# 我爱我家
page = 1
f.write('！！！我爱我家！！！\n\n')
i = 0
for place in areas:
	url = 'https://bj.5i5j.com/zufang/u1b0e6000n'+ str(page) + '/_'	
	# 网址后面的参数表示一些筛选条件，这里代表着整租和价位0-6k
	res = requests.get(url + place + '/')
	try:
		res.raise_for_status()
	except Exception as exc:
		print('Error! %s' % (exc))

	soup = BeautifulSoup(res.text, 'html.parser')
	for house in soup.select(".listCon"):
		title = house.h3.a.text
		href = house.h3.a['href']
		f.write('%d.\n%s\n%s' % (i, title, 'https://bj.5i5j.com' + href))
		for des in house.descendants:
			try:
				if 'i_01' in des.i['class']:
					f.write('%s' % (des.text))
				elif 'redC' in des['class']:
					f.write('%s' % (des.text))
			except:
				pass
	
		i += 1
		f.write('\n')
print('我爱我家写入完毕')

# 链家
f.write('\n\n')
f.write('！！！链家！！！\n\n')
i = 0
for place in areas:
	url = 'http://bj.lianjia.com/zufang/rt1erp6000rs'	# 整租和0-6k
	res = requests.get(url + place + '/')
	try:
		res.raise_for_status()
	except Exception as exc:
		print('Error! %s' % (exc))

	soup = BeautifulSoup(res.text, 'html.parser')
	for house in soup.select('.info-panel'):
		title = house.h2.a.text
		href = house.h2.a['href']
		f.write('%d.\n' % (i))
		f.write(title + '\t' + href + '\n')
		for des in house.descendants:
			try:
				if 'where' in des['class']:
					f.write(des.text + '\n')
				elif 'other' in des['class']:
					f.write(des.text + '\n')
				elif 'price' in des['class']:
					f.write('价格： ' + str(des.text) + '\n')
			except:
				pass

		i += 1
		f.write('\n')


f.close()
print('链家写入完毕')

#TODO: 豆瓣租房小组

