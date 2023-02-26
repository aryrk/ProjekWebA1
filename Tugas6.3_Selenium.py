from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from datetime import datetime
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
mainDriver = webdriver.Chrome(PATH)
secondDriver = webdriver.Chrome(PATH)
mainDriver.get("https://teknologi.bisnis.com/gadget")
list = []
i = 1
JmlPerulangan = 2

print(list)

for page in range(JmlPerulangan):
    for link in mainDriver.find_elements(By.XPATH, "(//div[@class='col-sm-8'])//h2//a"):
        print(link.text.split("\n"))
        secondDriver.get(link.get_attribute('href'))
        kategori = link.find_elements(By.XPATH,"(//div[@class='wrapper-description'])//div//a")
        judul = secondDriver.find_elements(By.CLASS_NAME, "title-only")
        deks = secondDriver.find_elements(By.CLASS_NAME, "subtitle")
        nama = secondDriver.find_elements(By.CLASS_NAME, "auth")
        img = secondDriver.find_elements(By.XPATH, "(//div[@class='main-image'])//img")
        tgl = secondDriver.find_elements(By.CLASS_NAME, "author")
        imgAuth = secondDriver.find_elements(By.XPATH, "(//div[@class='author'])//img")
        list.append(
            {"No": i,
             "Judul": judul[0].text.split("\n")[0],
             "Kategori":kategori[0].text.strip(),
             "Author": nama[0].text.split("\n")[0],
             "ImageAuthor": imgAuth[0].get_attribute("src"),
             "Image": img[0].get_attribute("src"),
             "Deskripsi": deks[0].text.split("\n")[0],
             "Published": tgl[0].text.split("\n")[1],
             "ScrappingDate": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
             }
        )
        i += 1

    btn = mainDriver.find_element(By.XPATH, "(//div[@class='btn-loadmore'])//a")
    mainDriver.get(btn.get_attribute('href'))
    time.sleep(3)

hasil_scraping = open("hasilnya.json", "w")
json.dump(list, hasil_scraping, indent=6)
hasil_scraping.close()

mainDriver.quit()
secondDriver.close()
