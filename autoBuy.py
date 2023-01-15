from blockchain import blockchain
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import random

load_dotenv()
password = os.environ["PASSWORD"]

# def buyAmazon(url):
#     driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")
#     driver.get(url)
#     time.sleep(15)
#     driver.find_element(By.ID, "buy-now-button").click()
#     time.sleep(300)

# def buyNoFrills(url):
#     driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")
#     driver.get(url)
#     pause = random.randint(5, 10)
#     time.sleep(pause)
#     driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/button').click()
#     time.sleep(50)

def Mockbuy(name, url):
    driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")
    driver.get(url)
    pause = random.randint(5, 10)
    time.sleep(pause)
    driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[3]/button').click()
    time.sleep(50)
    blockchain.add_new_transaction(["purchased {name}"])
    blockchain.mine()

#buyAmazon("https://www.amazon.ca/Squishmallow-Stuffed-Animal-Cuddle-Pillow/dp/B09QZ4X7ZV/ref=sr_1_1_sspa?crid=1FYB8GXU69HJ5&keywords=fox+squishmallow&qid=1673772947&sprefix=fox++sq%2Caps%2C87&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyS1BUUjhIODEySzlLJmVuY3J5cHRlZElkPUEwMzE0MzgyMlRMTlU5VjVZTEM5UyZlbmNyeXB0ZWRBZElkPUEwMDk3MTk0MTI3QVVYVk1XT1lUSCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
#buyNoFrills("https://www.nofrills.ca/scented-jasmine-rice/p/20121871_EA")           
