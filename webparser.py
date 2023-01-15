from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client
import time
import json
import os
from dotenv import load_dotenv
import random


load_dotenv()

purchase = {}

def extract_walmart_price(driver, url):
    driver.get(url)
    pause = random.randint(5, 10)
    time.sleep(pause)
    cost = driver.find_element(By.XPATH, '//*[@id="main-buybox"]/div[1]/div[3]/div/div[1]/div/div/div/span/span').text
    cost = cost[1:]
    return cost

def extract_nofrills_price(driver, url):
    driver.get(url)
    pause = random.randint(3, 10)
    time.sleep(pause)
    cost = driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div/span/span[1]').text
    cost = cost[1:]
    return cost

def extract_amazon_price(driver, url):

    driver.get(url)
    cost = driver.find_element(By.CLASS_NAME, "a-price-whole").text + "." + driver.find_element(By.CLASS_NAME, "a-price-fraction").text

    return cost

def notification(cost, name, platform):
    account_sid = os.environ["ACCOUNT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]
    twilio_num = os.environ["TWILIO_NUM"]
    receiver = os.environ["RECIEVER"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body=f""" Hey Good News! {name} has dropped to {cost} on {platform}!
                              \nGo Get It Now or reply to this text with "{name}" to automatically purchase it!
                              """,
                              from_=twilio_num,
                              to=receiver
    )

def writeJSON(productRecords, name="productRecords.json"):
    # Serializing json
    json_object = json.dumps(productRecords, indent=4)
    
    # Writing to sample.json
    with open(name, "w") as outfile:
        outfile.write(json_object)

def main():
    """This function will accept the search term and the maximum price you are
    expecting the product to be"""

    # startup the webdriver

    while True  :

        try:
            
            with open('productRecords.json') as db:
                productRecords = json.load(db)

        except:
            continue

        if productRecords:
            driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")
            for link in productRecords.keys():
                platform = productRecords[link]["platform"]
                price = productRecords[link]["price"]
                name = productRecords[link]["name"]
                
                if platform == "Amazon":
                    cost = extract_amazon_price(driver, link)
                    if float(cost) <= float(price):
                        notification(cost, name, platform)
                        purchase[name] = link
                        purchase["platform"] = platform
                        productRecords.pop(link)
                        writeJSON(productRecords)
                        writeJSON(purchase, "purchases.json")
                        break
                
                if platform == "Walmart":
                    cost = extract_walmart_price(driver, link)
                    if float(cost) <= float(price):
                        notification(cost, name, platform)
                        purchase[name] = link
                        purchase["platform"] = platform
                        productRecords.pop(link)
                        writeJSON(productRecords)
                        writeJSON(purchase, "purchases.json")
                        break
                
                if platform == "No Frills":
                    cost = extract_nofrills_price(driver, link)
                    if float(cost) <= float(price):
                        notification(cost, name, platform)
                        purchase[name] = link
                        purchase["platform"] = platform
                        productRecords.pop(link)
                        writeJSON(productRecords)
                        writeJSON(purchase, "purchases.json")
                        break

            time.sleep(random.randint(2, 10))
            driver.close()
        time.sleep(2)




if __name__ == '__main__':
    main()