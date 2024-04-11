from threading import Thread
from queue import Queue
from tqdm import tqdm
import requests
import time
import random

class WebsiteScraper:

  def __init__(self, companies):
    self.companies = companies
    self.counter = 0
  def search_site(self, company, queue, keyword):
    delay = random.uniform(.5, 1) 

    try:
      response = requests.get(company['jobs_page'])
      time.sleep(delay)
      if keyword in response.text:
        
         
         queue.put(company)
         print(f"{self.counter}. {company['jobs_page']}")
         self.counter += 1    
    

    except:
      queue.put(None)

  def search_sites(self, keyword):
    results = []
    queue = Queue()
    threads = []
    progress = tqdm(total=len(self.companies))

    for i, company in enumerate(self.companies):
      thread = Thread(target=self.search_site, args=(company, queue, keyword))
      threads.append(thread)
      thread.start()

    for thread in threads:
      thread.join()  

    while not queue.empty():
      result = queue.get()
      if result:
        results.append(result)
      progress.update()

    return results

