import requests 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

id = input('ID produktu:\n') 



driver = webdriver.Chrome()


# ------ DATART -----

driver.get("https://www.datart.cz/")

search = driver.find_element(By.CSS_SELECTOR, "#main-header > div.header-meta > div > div > form > div > input")

search.send_keys(id)

time.sleep(5)

search.send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "#c-p-bn").click()

datart_price = ""
datart_link = ""

time.sleep(5)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#snippet--searchProductList > div > div > div > div > div > div.product-box-info > div.product-box-buy-info > div.product-box-buy-info-cart > div.item-price > div > div.actual')))
    datart_price = driver.find_element(By.CSS_SELECTOR, "#snippet--searchProductList > div > div > div > div > div > div.product-box-info > div.product-box-buy-info > div.product-box-buy-info-cart > div.item-price > div > div.actual").text
except:
    datart_price = "Nenalezeno"

time.sleep(5)

if (datart_price != "Nenalezeno"):
    datart_link = driver.find_element(By.CSS_SELECTOR, "#snippet--searchProductList > div > div > div > div > div > div.product-box-top-side > div.item-title-holder > h3 > a").get_attribute("href")


print(datart_price + " link: " + datart_link)

# -----------------


# ------ ALZA -----

driver.get("https://www.alza.cz/")  

search = driver.find_element(By.CSS_SELECTOR, '#page > div:nth-child(6) > div > div > div.header-alz-1 > div > header > div.header-alz-6 > div > div.header-alz-104 > div > input')

time.sleep(5)

search.send_keys(id)

time.sleep(2)

search.send_keys(Keys.RETURN)

alza_price = ""
alza_link = ""


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'price-box__price')))
    alza_price = driver.find_element(By.CLASS_NAME, 'price-box__price').text
except:
    alza_price = "Nenalezeno"

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.name.browsinglink')))
    alza_link = driver.find_element(By.CSS_SELECTOR, ".name.browsinglink").get_attribute("href")
except:
    alza_link = "Nenalezeno"        

print(alza_price + " link: " + alza_link)

# -----------------


# ------ CZC -----

driver.get("https://www.czc.cz/")

driver.find_element(By.CSS_SELECTOR, "#ccp-popup > div > div.ccp-controls > button.btn.btn-link.js-reject-cookies").click()

time.sleep(1)

search = driver.find_element(By.XPATH, '//*[@id="fulltext"]')

search.send_keys(id)

search.send_keys(Keys.RETURN)

czc_price = ""
czc_div = ""
czc_link = ""

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tiles > div > div.overflow > div.price-wrapper > div > div > span')))
    czc_div = driver.find_element(By.CSS_SELECTOR, '#tiles > div > div.overflow > div.price-wrapper > div > div > span')
except:
    czc_div = "Nenalezeno"

try:
    czc_price = czc_div.find_elements(By.XPATH, '*')
except:
    czc_price = "Nenalezeno"

if (czc_div != "Nenalezeno"):
    czc_link = driver.find_element(By.CLASS_NAME, "tile-title").find_element(By.CSS_SELECTOR, "h5 > a").get_attribute("href")
else:
    czc_link = "Nenalezeno"


try:
    print(czc_price[1].text + " link: " + czc_link)
except:
    print("Nenalezeno" + " link: " + czc_link)






