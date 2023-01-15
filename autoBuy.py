from blockchain import Blockchain
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from flask import Flask, request
import json
import random
import time


load_dotenv()


blockchain = Blockchain()

def Mockbuy(name, url):
    driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")
    driver.get(url)
    pause = random.randint(3, 5)
    time.sleep(pause)
    driver.find_element(By.ID, 'buy-btn').click()
    time.sleep(pause)
    name = driver.find_element(By.ID, 'name')
    name.send_keys("Benjamin Sun")
    time.sleep(1)
    address = driver.find_element(By.ID, 'address')
    address.send_keys("176 Haddon Ave S")
    time.sleep(1)
    card_num = driver.find_element(By.ID, 'card-num')
    card_num.send_keys("111111111111")
    time.sleep(1)
    card_exp = driver.find_element(By.ID, 'card-exp')
    card_exp.send_keys("12/22")
    time.sleep(1)
    cvv = driver.find_element(By.ID, 'card-cvv')
    cvv.send_keys("133")
    time.sleep(1)
    driver.find_element(By.ID, 'place-order').click()
    time.sleep(5)

    transaction = f"Benjamin Sun purchased {name}"
    blockchain.create_block_from_transaction([transaction])

app = Flask(__name__)


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    hashes = []
    for block in blockchain.chain:
        chain_data.append(block.block_data)
        hashes.append(block.block_hash)
    
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data,
                       "hash": hashes})



app.run(debug=True, port=8080)