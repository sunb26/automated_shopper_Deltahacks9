from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By





def extract_record(single_item):

    price_parent = single_item.find("span", "a-price")

    price = price_parent.find("span", "a-offscreen").text

    return price

def main():
    """This function will accept the search term and the maximum price you are expecting the product to be"""

    # startup the webdriver

    prices_list = []
    options=Options()
    
    options.headless = True #choose if we want the web browser to be open when doing the crawling 
    driver = webdriver.Chrome(r"C:\Users\bsun7\OneDrive\Documents\chromedriver\chromedriver.exe")


    url = "https://www.amazon.ca/Cartoon-Flowers-Decorative-Butterfly-Included/dp/B0BKLX8YNF/ref=sr_1_7?crid=2JLNPARB191E&keywords=fox+pillow&qid=1673737691&sprefix=fox+pillo%2Caps%2C87&sr=8-7" # takes the search term to get_url() function above.

    driver.get(url)
    cost = driver.find_element(By.CLASS_NAME, "a-price-whole").text + "." + driver.find_element(By.CLASS_NAME, "a-price-fraction").text

    print(cost)

    driver.close()

if __name__ == '__main__':
    main()