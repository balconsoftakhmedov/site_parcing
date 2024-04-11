from io import BytesIO
import json

with open('data.json', 'rb') as f:
  data = json.load(BytesIO(f.read()))

companies = []

for table in data['data']['tableDatas']:

  for row in table['rows']:

    cell_values = row.get('cellValuesByColumnId', {})
    
    company = {
      'name': None,
      'website': None,
      'linkedin': None,
      'jobs_page': None,
      'countries': None
    }
    
    if 'fldbWJrMP9MLZzmIU' in cell_values:
      company['name'] = cell_values['fldbWJrMP9MLZzmIU']
      
    if 'fld2BL08lp9YptaLE' in cell_values:
      company['website'] = cell_values['fld2BL08lp9YptaLE']
      
    if 'fldKKoRYPWB6zPMUu' in cell_values:
      company['linkedin'] = cell_values['fldKKoRYPWB6zPMUu']
      
    if 'fldAcYWg25vbz5su7' in cell_values:
      company['jobs_page'] = cell_values['fldAcYWg25vbz5su7']
      
    if 'fldzy3VdpGZrPEY8n' in cell_values:
      company['countries'] = cell_values['fldzy3VdpGZrPEY8n']

    companies.append(company)

 
# Write companies list to file
with open('companies.json', 'w') as f:
   json.dump(companies, f, indent=2)




