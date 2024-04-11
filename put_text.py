import re 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(options=options)

url = 'https://airtable.com/embed/appeUaq03QhH6Nx3v/shrUNL8lG6zekaNqi/tbl7mpWPX2MQAMZ2E/viwnjW20B6oojJuqN?backgroundColor=purple&blocks=hide'

driver.get(url)
time.sleep(30) 

soup = BeautifulSoup(driver.page_source, 'html.parser')


# Extract <body> HTML as before
body = soup.find('html')

# Remove <style> tags
for style in body.find_all('style'):
    style.decompose()


# Get cleaned HTML as string
body_html = str(body)



# Write as UTF-8 to handle encodings
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(body_html)




driver.quit()
