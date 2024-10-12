import selenium.webdriver.chrome.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
options=options)
driver.get("https://emalls.ir/")

//*[@id="ContentPlaceHolder1_rptMainSlider_DivSlideItem_0"]/div/img

//*[@id="ContentPlaceHolder1_rptMainSlider_DivSlideItem_0"]/div/img