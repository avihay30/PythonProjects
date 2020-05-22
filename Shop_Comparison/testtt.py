from time import sleep
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import scrapy

# if __name__ == '__main__':
    # # req = Request("http://www.victoryonline.co.il/Ajax/FetchUserControl.aspx?UserControl=Popup_NgProductDetails&ProductID=71909", headers={'User-Agent': 'Mozilla/5.0'})
    # # page = urlopen(req).read()
    # chrome_options = Options()
    # chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("disable-infobars")
    # chrome_options.add_argument("--disable-extensions")
    #
    # driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
    # # driver.get("https://www.rami-levy.co.il/default.asp?isjson=true&catid={2C0A7C7F-06FF-4B03-AC0C-99A663300055}&details_type=1&itemid={7D15D537-F57C-432E-BBA6-5F71372FFC7F}")
    # driver.get("https://www.mysupermarket.co.il/Ajax/FetchUserControl.aspx?UserControl=Popup_NgProductDetails&ProductID=1499&TrackingCode=111.5BvUGPMH2U2NvebeG3MENw")
    # sleep(3)
    # # driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]').click()
    # # driver.
    # sleep(2)
    # soup = BeautifulSoup(driver.page_source, "html.parser")

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.mysupermarket.co.il/Ajax/FetchUserControl.aspx?UserControl=Popup_NgProductDetails&ProductID=1499']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            print(brickset)
            pass
