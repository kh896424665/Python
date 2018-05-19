# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
import urllib
from multiprocessing import Queue
import threading
import random
from time import sleep
User_Agent=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36","Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]

HEADERS = {
    'User-Agent':  User_Agent[random.randint(0,4)],
    # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/201002201 Firefox/55.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
csvfile = open('去哪儿景点.csv','w',encoding='utf-8', newline='')
writer = csv.writer(csvfile)
writer.writerow(["区域","名称","景点id","类型","级别","价格","热度","地址","特色","经纬度","经度","纬度","图片"])


def download_page(url):  # 下载页面
    try:
        data = requests.get(url, headers=HEADERS, allow_redirects=True).content  # 请求页面，获取要爬取的页面内容
        return data
    except:
        pass


#下载页面 如果没法下载就 等待1秒 再下载
def download_soup_waitting(url):
    try:
        response= requests.get(url,headers=HEADERS,allow_redirects=False,timeout=5)
        if response.status_code==200:
            html=response.content
            html=html.decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            return soup
        else:
            sleep(1)
            print("等待ing")
            return download_soup_waitting(url)
    except:
        return ""

def getTypes():
    types=["文化古迹","自然风光","公园","古建筑","寺庙","遗址","古镇","陵墓陵园","故居","宗教"] #实际不止这些分组 需要自己补充
    for type in types:
        # url="http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest&subject="+type+"&page=1"
        url = "http://piao.qunar.com/ticket/list.htm?keyword=%E8%A5%BF%E5%AE%89&region=&from=mpl_search_suggest&subject="+type+"&page=1"
        getType(type,url)

def getType(type,url):
    soup=download_soup_waitting(url)
    search_list=soup.find('div', attrs={'id': 'search-list'})
    sight_items=search_list.findAll('div', attrs={'class': 'sight_item'})
    path= "E:\git\Python\pystudy\qunarSpider\image"   #设置图片存放路径
    paths = path + '\\'
    for sight_item in sight_items:
        print(sight_item)
        name=sight_item['data-sight-name']   #景点名
        districts=sight_item['data-districts']  #区域
        point=sight_item['data-point']     #经纬度
        longitude = point.split(",")[0]   #精度
        latitude= point.split(",")[1]   #纬度
        address=sight_item['data-address']   #地址
        data_id=sight_item['data-id']      #景点ID
        data_img=sight_item['data-sight-img-u-r-l']  #景点图片地址
        urllib.request.urlretrieve(data_img, '{0}{1}.jpg'.format(paths,name))  #下载图片

        level=sight_item.find('span',attrs={'class':'level'})   #景点级别
        if level:
            level=level.text
        else:
            level=""

        product_star_level=sight_item.find('span',attrs={'class':'product_star_level'})   #景点热度
        if product_star_level:
            product_star_level=product_star_level.text[3:]
        else:
            product_star_level=""
        #print(product_star_level)

        price = sight_item.find('span', attrs={"class": 'sight_item_price'})  #门票价格
        if price:
            price = price.text
            price = price[1:-2]
        else:
            price =""
        #print(price)

        intro=sight_item.find('div',attrs={'class':'intro'})    #景点介绍
        if intro:
            intro=intro['title']
        else:
            intro=""
        writer.writerow([districts.replace("\n",""),name.replace("\n",""),data_id.replace("\n",""),type.replace("\n",""),level.replace("\n",""),price.replace("\n",""),product_star_level.replace("\n",""),address.replace("\n",""),intro.replace("\n",""),point.replace("\n",""),longitude.replace("\n",""),latitude.replace("\n",""),data_img.replace("\n","")])
    next=soup.find('a',attrs={'class':'next'})
    if next:
        next_url="http://piao.qunar.com"+next['href']
        getType(type,next_url)


if __name__ == '__main__':
    getTypes()
print("爬取完成！")