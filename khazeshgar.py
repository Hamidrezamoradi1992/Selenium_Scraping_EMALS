from selenium.common import JavascriptException, NoSuchElementException, ElementNotInteractableException, \
    InvalidElementStateException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver.chrome import ChromeDriverManager
#service=ChromeService(ChromeDriverManager().install()),options=options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
import time

class Emalls_Selenium:
    bank = []

    def __init__(self, name_product):
        self.products = name_product
        self.driver = webdriver.Chrome()
        self.driver.get('https://emalls.ir/')
        time.sleep(3)

    def __enter__(self):
        self.i = 0
        self.d = 0
        self.driver.find_element(By.ID, 'ContentPlaceHolder1_SearchInBottom_txtSearch').send_keys(self.products)
        self.driver.find_element(By.ID, 'ContentPlaceHolder1_SearchInBottom_txtSearch').send_keys(Keys.ENTER)
        time.sleep(3)
        for i in (c := self.driver.find_elements(By.CSS_SELECTOR, '#listdiv .prd-info >div >h2 a')):
            i.send_keys(Keys.ENTER)
            time.sleep(5)
            try:
                self.driver.execute_script('document.querySelector("#btnshowhide").click()')
            except JavascriptException:
                pass
            time.sleep(1)
            url_picture=self.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_rptMainSlider_DivSlideItem_0'
                                                           '"]/div/img').get_attribute("src")
            name_product = self.driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_H1TitleDesktop')
            print(str(name_product.text))
            self.d = len(list(self.driver.find_elements(By.CSS_SELECTOR, '.box-data .shoplist .shop-row')))
            j=5
            for ll in self.driver.find_elements(By.CSS_SELECTOR, '.box-data .shoplist .shop-row'):
                name_shops = ll.find_element(By.CSS_SELECTOR,
                                             '.box-data .shoplist .shop-row .shop-logo-wrapper .shopnamespan a').text

                if len(c := name_shops.split("\n")) > 1:
                    name_shop = c[0]
                elif len(name_shops.split("\n")) == 0:
                    name_shop = "no name"
                else:
                    name_shop = name_shops
                try:
                    product_price = ll.find_element(By.CSS_SELECTOR,
                                                    '.box-data .shoplist .shop-row .shop-prd-price .flx-berooz .shop-price-div a').text
                    price = product_price.split("\n")
                    c = str(price[len(price) - 1]).split(",")
                    if len(c) >= 2:
                        price2 = int("".join(c))
                except NoSuchElementException:
                    price2 = 0

                try:

                    urlss = ll.find_element(By.CSS_SELECTOR,
                                            '.box-data .shoplist .shop-row .shop-prd-price .shop-btns >a.btn.shop-button')
                    self.driver.execute_script('arguments[0].removeAttribute("target")', urlss)
                    urlss.send_keys(Keys.ENTER)
                    time.sleep(3)
                    url = self.driver.current_url
                    self.driver.back()
                    time.sleep(2)
                except (NoSuchElementException , NoSuchElementException,ElementNotInteractableException,InvalidElementStateException):
                    url=self.driver.current_url
                self.__class__.bank.append((str(name_product.text), str(name_shop), price2, url,url_picture))
                j -= 1
                if j==1:
                    break



            self.driver.back()
            time.sleep(1)
            if self.i == 1:
                break
            break
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        for i in self.__class__.bank:
            if i[2]>0:
                print(i[0], i[1], i[2], i[3] ,f"url pic:{i[4]}", sep='\n')
        # database call
        return self.__class__.bank


