from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

startUrl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/robot/Downloads/chromedriver_win32/chromedriver.exe")
browser.get(startUrl)
time.sleep(10)


def scrape():
    headers = ["NAME", "LIGHT_YEARS_FROM_EARTH", "PLANET_MASS", "STELLAR_MAGNITUDE", "DISCOVERY_DATE"]
    planetData = []
    for i in range(0,10):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={"class","exoplanet"}):
            liTags = ultag.find_all("li")
            tempList = []
            for index,litag in enumerate(liTags):
                if index == 0:
                    tempList.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempList.append(litag.contents[0])
                    except:
                        tempList.append("")
            planetData.append(tempList)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Scrapper.csv","w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planetData)
scrape()