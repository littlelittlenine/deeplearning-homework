import requests
from bs4 import BeautifulSoup
import os
#Explanation: This version is the version I originally completed in 10.1, but it simply implements the function, and does not combine with the UI
#Crawl the dblp website

url='https://dblp.org/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200'}
response=requests.get(url,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='link',attrs={"rel":'search'})
web=str(table['href'])
#print(web)
#######After crawling the DBLP website, find its search function file and replace the search keywords
url=web
#print(url)
response=requests.get(url,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='url',attrs={"type":'text/html'})
#if table:
#    url_template = str(table['template'])
#    print(url_template)
#else:
#    print("未找到名为'Url'的标签")
url_template=str(table['template'])
#print(url_template)
search_term="Ya-Qin Zhang"
search_url = url_template.replace("{searchTerms}", search_term)
####Continuing to crawl with the new URL is equivalent to searching for the name of the relevant scientist on the page
response=requests.get(search_url,headers=headers)
if response:
    print("找到了")
bs=BeautifulSoup(response.content,"html.parser")
table=bs.find(name='nav',attrs={"class":'header'})
item=table.find('a')
web_name=str(item['href'])
print(web_name)
response=requests.get(web_name,headers=headers)
bs=BeautifulSoup(response.content,"html.parser")
#print(bs)
table=bs.find(name='url')
web_name2=table.text
print(web_name2)
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
    file_path = "D:\\360MoveData\\Users\\keven\\Desktop\\downloaded_file.bib"
    with open(file_path, "wb") as file:
        file.write(response.content)
    print("文件下载成功！")
else:
    print("文件下载失败！")
