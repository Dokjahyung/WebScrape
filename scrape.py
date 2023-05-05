from bs4 import BeautifulSoup
from selenium import webdriver
import statistics
import time
 
#this is a test of the webscrape beautiful soup library
def shop2():
   PATH = r'usercode/chromedriver'
   driver = webdriver.Chrome(PATH)
   driver.get("https://www.madewell.com/womens/clothing/jeans")
 
   soup = BeautifulSoup(driver.page_source, 'html.parser')
   response = soup.find_all("span", "product-sales-price product-usd")
  
   data = []
 
   for item in response:
       data.append(float(item.text.strip("\n$")))
 
   print(data)
   return data

while True:
    time.sleep(5)
    extracted_data2 = shop2()
    
    print(statistics.mean(extracted_data2))
