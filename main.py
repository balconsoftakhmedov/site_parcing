from company_data import CompanyData
from website_scraper import WebsiteScraper
import json

data = CompanyData('companies.json')

# Create scraper 
scraper = WebsiteScraper(data.companies)  

# Call search method
results = scraper.search_sites('wordpress')

with open('needed_urls.txt', 'w') as f:

  if results:

    for result in results:
      
      f.write(result['name'] + ' ' + result['linkedin'] + ' ' + result['jobs_page']+ ' ' + '\n')

  else:

    f.write('No results found')

