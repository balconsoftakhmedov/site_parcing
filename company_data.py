import json

class CompanyData:

  def __init__(self, file_name):
    self.companies = self.load_data(file_name)  

  def load_data(self, file_name):

    with open(file_name) as f:
      data = json.load(f)

    companies = []

    for company in data:
      companies.append({
        'name': company['name'],
        'jobs_page': company['jobs_page'],
        'linkedin':company['linkedin'],
      })
    
    return companies
