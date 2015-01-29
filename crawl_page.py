#coding:utf-8

import requests
from lxml import etree
from make_url import *
import json


def fetch_html(urls):
    man_list = []
    for url in urls:
        r = requests.get(url)
        if r.status_code == 200:
            html = r.text
            tree = etree.HTML(html)
    
	    name_kr = tree.xpath("//div[@class = 'profile']/h4/text()")[0]
	    name_kr = clean_data(name_kr)
	    name_cn = tree.xpath("//div[@class = 'profile']/ul/li[2]/text()")[0]
	    name_cn = clean_data(name_cn)
	    name_en = tree.xpath("//div[@class = 'profile']/ul/li[3]/text()")[0]
	    name_en = clean_data(name_en)
	    birth = tree.xpath("//div[@class = 'profile']/ul/li[4]/text()")[0]
	    birth = clean_data(birth)
	    party = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[1]/text()")[0]
	    party = clean_data(party)
	    district = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[2]/text()")[0]
	    district = clean_data(district)
	    committee = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[3]/text()")[0]
	    committee = clean_data(committee)
	    elected_number = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[4]/text()")[0]
	    elected_number = clean_data(elected_number)
	    office_phone = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[5]/text()")[0]
	    office_phone = clean_data(office_phone)
	    try:
	    	homepage = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd/a/text()")[0].encode("utf-8")
	    except  IndexError:
		homepage = None
	    try:
	    	mail_add = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[7]/text()")[0]
		mail_add = clean_data(mail_add)
	    except  IndexError:
		mail_add = None	
	    aides = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[8]/text()")[0]
	    aides = clean_data(aides)
	    scr1 = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[9]/text()")[0]
	    scr1 = clean_data(scr1)
	    scr2 = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[10]/text()")[0]
	    scr2 = clean_data(scr2)
	    try:
	        hobby = tree.xpath("//li[@class = 'right']/dl[@class = 'pro_detail']/dd[11]/text()")[0]
		hobby = clean_data(hobby)
	    except IndexError:
	        hobby = None
    
	    man_dict =   {'name_kr' : name_kr,    'name_cn' : name_cn,    'name_en' : name_en,  'birth' : birth,    'party' : party, 'district' : district,     'committee' : committee,    'elected_number' : elected_number,   'office_phone' : office_phone,   'homepage' : homepage,  'mail_add' : mail_add,  'aides' : aides,   'scr1' : scr1,  'scr2' : scr2,   'hobby' : hobby }
	    with open("list.json","w") as f:		
	    	json.dump(man_dict,f)
	    man_list.append(man_dict)
		    
    return man_list
	
def clean_data(data):
	data = data.replace("\t","").replace("\r","").replace("\n","").replace(" ","").encode("utf-8")

	return data




def main():
    urls = full_list_page()
    crawl = fetch_html(urls)

    return crawl







if __name__ == "__main__":
   print main()
