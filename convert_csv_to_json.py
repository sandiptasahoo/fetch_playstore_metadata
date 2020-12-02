import csv
import json
  
  
# Function to convert a CSV to JSON
def make_json(csvFilePath, jsonFilePath):
      
    # create a dictionary
    data = {}
      
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-16', errors='ignore') as csvf:
        csvReader = csv.DictReader(csvf)
        rows = list(csvReader)
  
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(rows, indent=4))

csvFilePath = '/Users/xxxx/xxxx/xxxx.csv'
jsonFilePath = '/Users/xxxx/xxxx/xxx/xxxx.json'
  
# Call the make_json function
make_json(csvFilePath, jsonFilePath)
