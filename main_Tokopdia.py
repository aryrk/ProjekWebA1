import requests
import json
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
maxPage = 6

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

result = []
id = 1

for page_num in range(1, maxPage):  # ambil data dari 5 halaman awal
    URL = f"https://www.tokopedia.com/p/komputer-laptop/laptop/ultrabook?page={page_num}"
    page = requests.get(URL, headers=headers)  # mengunduh halaman
    soup = BeautifulSoup(page.content, "html.parser")  # ekstraksi kode html
    tokopedia = soup.find(class_="css-13l3l78 e1nlzfl9")  # mengambil produk

    # BAGIAN ISI
    title = tokopedia.find_all("span", class_="css-1bjwylw")
    discount = tokopedia.find_all("div", class_="css-rn1hus")
    priceBeforeDisc = tokopedia.find_all("div", class_="css-rn1hus")
    priceAfterDisc = tokopedia.find_all("span", class_="css-o5uqvq")
    infoToko = tokopedia.find_all("span", class_="css-1kr22w3")
    button = tokopedia.find_all("a", class_="css-89jnbj")

    # BAGIAN ISI
    j = 0
    for i in range(len(title)):
        tempDiscount = "0%"
        tempPrice = priceAfterDisc[i].text.strip()
        try:
            tempDiscount = discount[i].text.strip().split("%")[0]
            tempPrice = discount[i].text.strip().split("%")[1]
        except IndexError:
            tempDiscount = "0"

        result.append(
            {"id": id,
             "produk": title[i].text.strip(),
             "diskon": tempDiscount+"%",
             "hargasebelumdiskon": tempPrice,
             "hargasetelahdiskon": priceAfterDisc[i].text.strip(),
             "tempattoko": infoToko[j].text.strip(),
             "namatoko": infoToko[j+1].text.strip(),
             "link": button[i].attrs['href'],
             "time": today.strftime("%d/%m/%Y"),
             }
        )
        j += 2
        id += 1

HasilJSON = json.dumps(result, indent=4)
JSONFile = open("ultrabook.json", "w")
JSONFile.write(HasilJSON)
JSONFile.close()
