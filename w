import json

with open('data.json') as f:
  data = json.load(f)

companies = []

for table in data['data']['tableDatas']:

  # Extract company info 
  company = {
    'name': table['rows'][0]['cellValuesByColumnId']['fldbWJrMP9MLZzmIU'],
    'website': table['rows'][0]['cellValuesByColumnId']['fld2BL08lp9YptaLE'],
    'linkedin': table['rows'][0]['cellValuesByColumnId']['fldKKoRYPWB6zPMUu'],
    'jobs_page': table['rows'][0]['cellValuesByColumnId']['fldAcYWg25vbz5su7'],
    'countries': table['rows'][0]['cellValuesByColumnId']['fldzy3VdpGZrPEY8n'] 
  }
  
  # Extract job roles
  roles = [
    role['foreignRowDisplayName'] 
    for role in table['rows'][0]['cellValuesByColumnId']['fld9nF32JiU35eyXD']
  ]

  company['roles'] = roles

  # Add company data to list
  companies.append(company)

# Write companies list to JSON  
with open('companies.json', 'w') as f:
  json.dump(companies, f, indent=2)