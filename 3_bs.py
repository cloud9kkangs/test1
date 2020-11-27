import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/detail.nhn?titleId=183559&no=63&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
