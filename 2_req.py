import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status

# if(res.status_code = requests.codes.ok)
#     print("정상입니다")
print(len(res.text))

with open("ghome.html", "w", encoding="utf8") as f:
    f.write(res.text)