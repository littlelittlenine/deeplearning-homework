###相较于第一次的内容，这次修改是实现能够将.BIB文件下载到指定的位置，同时加上了页面设计，

import requests
from bs4 import BeautifulSoup
import os

#爬取dblp网站

url='https://dblp.org/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'}
response=requests.get(url,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='link',attrs={"rel":'search'})
web=str(table['href'])
#print(web)
#######爬取DBLP网站后，找到其搜索功能文件，替换搜索关键词
url=web
#print(url)
response=requests.get(url,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='url',attrs={"type":'text/html'})
#if table:
#url_template = str(table['template'])
#    print(url_template)
#else:
#    print("未找到名为'Url'的标签")
url_template=str(table['template'])
print(url_template)
search_term="YaQing Zhang"
search_url = url_template.replace("{searchTerms}", search_term)
####用得到的新网址继续爬取，相当于你在网页中搜索了相关科学家姓名
response=requests.get(search_url,headers=headers)
if response:
    print("找到了")#######################
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='nav',attrs={"class":'header'})
item=table.find('a')
####进入准确查找网页
web_name=str(item['href'])
print(web_name)################
response=requests.get(web_name,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
print(bs)
table=bs.find(name='url')
web_name2=table.text
print(web_name2)#########################
response=requests.get(web_name2,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='nav',attrs={"class":'head'})
sub_tags=table.find_all(name='div',attrs={"class":'head'})
target_element = "bibtex"
for sub_tag in sub_tags:
    if target_element in str(sub_tag):
        url = sub_tag.find('a')['href']
#        print(url)
        break
response=requests.get(url,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
sub_tags=bs.find_all(name='p')
target_element = ".bib"
for sub_tag in sub_tags:
    if target_element in str(sub_tag):
        url = sub_tag.find('a')['href']
#        print(url)
#print(table.text)
response = requests.get(url)
if response.status_code == 200:
    file_path = input("请输入地址名：")
    with open(file_path, "wb") as file:
        file.write(response.content)
    print("文件下载成功！")
else:
    print("文件下载失败！")

