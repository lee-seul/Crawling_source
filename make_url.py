#coding:utf-8

import requests
from lxml import etree
from urlparse import urljoin

def list_page(url):
    r = requests.get(url)
    if r.status_code == 200:
      html = r.text
      tree = etree.HTML(html)
      urls_list = tree.xpath("//dd/a/@onclick")
      url_parameter = []
      for url in urls_list:
          urls = url[9:-1]
          url_parameter.append(urls)

    return url_parameter

def full_url(url_parameter):
    base_url = 'http://www.assembly.go.kr/assm/memPop/memPopup.do?dept_cd='
    craw_url = []
    urls = ''
    for url in url_parameter:
        urls = base_url + str(url)
        craw_url.append(urls)

    return craw_url

def main():
    url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=500'
    urls = full_url(list_page(url))

    return urls

if __name__ == "__main__":
   print main()
