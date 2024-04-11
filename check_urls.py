from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from bs4 import BeautifulSoup
import time

chrome_options = Options()
chrome_options.headless = True

urls = ['https://hellonewjob.org/post/400-companies-from-hellonewjob']

for url in urls:

  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)

  time.sleep(25) 

  soup = BeautifulSoup(driver.page_source, 'html.parser')

  if soup.find(string=lambda text: "wordpress" in text.lower()):
    print(f"Wordpress found on page: {url}")
  
  else:
    print(f"Wordpress NOT found on page: {url}")

  driver.quit() 
