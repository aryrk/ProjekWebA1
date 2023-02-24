import requests
import json
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

URL = f"https://www.tokopedia.com/p/komputer-laptop/laptop/ultrabook"
page = requests.get(URL, headers=headers)  # mengunduh halaman
soup = BeautifulSoup(page.content, "html.parser")  # ekstraksi kode html
tokopedia = soup.find(class_="css-13l3l78 e1nlzfl9")  # mengambil produk

title = tokopedia.find_all("span", class_="css-1bjwylw")

link = tokopedia.find_all("img")

images = [link["src"] for link in link]

print(images)

result = []
# for i in range(len(title)):
#     result.append({"imgurl": images[i]})
# print(result)