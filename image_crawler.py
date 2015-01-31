#-*-coding:utf-8-*-

import requests
from lxml import etree


def image_crawler(url):
	html = requests.get(url)
	tree = etree.HTML(html.text)

	img_xpath = tree.xpath("//a/img/@src")
	for img in img_xpath:
		img_url = 'http://www.assembly.go.kr' + str(img)
		response = requests.get(img_url)
		f = open('downloaded_images/%s'% img[7:],'wb')
		f.write(response.content)
		f.close()


if __name__ == "__main__":
	url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=500'
	image_crawler(url)


