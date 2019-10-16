from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import time

class Price():
    def __init__(self):
        self.chromeOptions = Options()
        self.chromeOptions.headless = True

    def parsePrice(self):
        url = 'https://finance.yahoo.com/quote/NOK?p=NOK&.tsrc=fin-srch'
        path = os.getcwd() + '/chromedriver'

        driver = webdriver.Chrome(executable_path = path, options=self.chromeOptions)
        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find_all("div", class_="My(6px) Pos(r) smartphone_Mt(6px)")[0].find('span').text

        #time.sleep(30)
        driver.quit()

        return price


#print(Price().parsePrice())
