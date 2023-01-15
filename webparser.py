from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")

def extract_walmart_price(url):
    driver.get(url)
    cost = driver.find_element(By.XPATH, r'//*[@id="main-buybox"]/div[1]/div[4]/div/div[1]/div/div/div/span/span').text

    return cost

def extract_amazon_price(url):

    driver.get(url)
    cost = driver.find_element(By.CLASS_NAME, "a-price-whole").text + "." + driver.find_element(By.CLASS_NAME, "a-price-fraction").text

    return cost

def main():
    """This function will accept the search term and the maximum price you are
    expecting the product to be"""

    # startup the webdriver

    options=Options()
    
    options.headless = True #choose if we want the web browser to be open when doing the crawling 



    cost = extract_walmart_price("https://www.walmart.ca/en/ip/pediasure-complete-nutritional-supplement-4-x-235-ml-vanilla-kids-nutritional-shake-containing-dha-and-vitamins-helps-promote-weight-gains-when-taken-/6000017348400")

    print(float(cost[1:]))

if __name__ == '__main__':
    main()