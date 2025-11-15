from bs4 import BeautifulSoup 
import requests

soup = BeautifulSoup("<p>Some<b>bad<i>HTML","html.parser")
print(soup.prettify())
a=soup.find(text="asghar")
print(a)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
div=soup.find("a")
print(div)
print(soup.p)
print(soup.p.string)
print(soup.a.string)
a=soup.find_all('a')
print(a)
print(a[1].string)
a=soup.find(id="link3")
print(a.string)
print(soup.get_text())

"""https://opencv.org/blog/top-python-libraries/"""

html=requests.get("https://builtin.com/articles/types-of-computers")
html_doc=html.text

soup = BeautifulSoup(html_doc, 'html.parser')
title=soup.find_all("h2")
print(title[1].string)
h2_list=soup.find_all("h3")
print(h2_list)
l=[]
for x in h2_list[:6]:
   print(x.string) 
print(l[1].string)
