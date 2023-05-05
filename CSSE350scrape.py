from bs4 import BeautifulSoup
from selenium import webdriver
import statistics
import time
import tkinter as tk
 
 
counter = 0

def validate_range(data):
    global counter
    counter += 1
    count = str(counter)
    l3.config(text="Updated: " + count)
    if ((data <= 100) or (data >= -100)) :
        l2.config(text="Data validated") 
        print("Data validated")
        return True
    
    l2.config(text="Unable to validate data")
    print("Unable to validate data")
    return False

def GM_motors():
   PATH = r'usercode/chromedriver'
   driver = webdriver.Chrome(PATH)
   driver.get("https://www.google.com/search?q=general+motors+stock+price&sxsrf=APwXEdcsJQ_t3GnLcEs19y7UQcNY0KsEhQ%3A1683234473262&ei=qR5UZIfED72Mur8Pj4mEgAw&ved=0ahUKEwjHvOiGydz-AhU9hu4BHY8EAcAQ4dUDCBA&uact=5&oq=general+motors+stock+price&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6CggAEIoFELADEEM6DQgAEOQCENYEELADGAE6FQguEIoFEMcBENEDEMgDELADEEMYAjoPCC4QigUQyAMQsAMQQxgCOgcIABCKBRBDOg0ILhCKBRDHARDRAxBDOg0IABCKBRCxAxCDARBDOg4ILhDHARCxAxDRAxCABDoKCAAQigUQsQMQQzoQCAAQgAQQsQMQgwEQRhD6AUoECEEYAFCJDljMGmCEG2gBcAF4AIABd4gBzQeSAQM5LjKYAQCgAQHIARPAAQHaAQYIARABGAnaAQYIAhABGAg&sclient=gws-wiz-serp")
 
   soup = BeautifulSoup(driver.page_source, 'html.parser')
   response = soup.find("span", "IsqQVc NprOob wT3VGc")
   
   data = float(response.text.strip("\n$"))

   if (validate_range(data) == True):
    return data

def update_label():
    extracted_data2 = GM_motors()
    l1.config(text = extracted_data2)
    window.after(5000, update_label)
    print(extracted_data2)

window = tk.Tk()
window.title("webScrapeCSSE350")
window.geometry("400x300")

l1 = tk.Label(window, text="initializing web scrape...")
l1.pack()
l2 = tk.Label(window, text="validating updated info...")
l2.pack()
l3 = tk.Label(window, text="Updated: ")
l3.pack()

update_label()

window.mainloop()
