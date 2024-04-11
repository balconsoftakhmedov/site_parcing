from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()

url = 'https://masterstudy.stylemixthemes.com/lms-plugin/'
driver.get(url)

# Wait for page to fully render with JavaScript
time.sleep(5) 

soup = BeautifulSoup(driver.page_source, 'html.parser')

# Now soup contains the full HTML after JavaScript execution
# You can parse normally with BeautifulSoup

# Search for wordpress in rendered HTML


results = soup.find_all(string=lambda text: "wordpress" in text.lower())


for result in results:
    print(result)

driver.quit()

