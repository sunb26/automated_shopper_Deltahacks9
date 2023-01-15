import blockchain
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()
password = os.environ["PASSWORD"]

def buyAmazon(url):
    driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")
    driver.get(url)
    driver.find_element(By.ID, "buy-now-button").click()
    time.sleep(5)
    email = driver.find_element(By.XPATH, '//*[@id="ap_email"]').click()
    email.send_keys("bsun7197@gmail.com")
    time.sleep(8)
    driver.find_element(By.ID, "continue").click()
    time.sleep(3)
    passwordField = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    passwordField.send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()
    driver.find_element(By.XPATH, '//*[@id="orderSummaryPrimaryActionBtn"]/span/input').click()
    driver.find_element(By.XPATH, '//*[@id="orderSummaryPrimaryActionBtn"]/span/input')
    

            
