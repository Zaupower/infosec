'''
Consider a “.csv” file with 4 columns, Department, Name, Role, Salary. Read the file and
organize the data into a dictionary (each department should be stored as key and the
corresponding value should be a list of dictionaries containing employee’s name, role, and
salary). Save the contents of the dictionary as an indented “. json” file.
a. Hint: open(), split(), json.dump()
b. What is JSON Standard?
'''

import csv
import json
csvFilePath = './supportfiles/ex9.csv'
jsonFilePath = './supportfiles/ex9.json'
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for row in csvReader:
            department = row['Department']
            name = row['Name']
            role = row['Role']
            salary = row['Salary']
            if department in data:
                data[department].append({'Name': name, 'Role': role, 'Salary': salary})
            else:
                data[department] = [{'Name': name, 'Role': role, 'Salary': salary}]


    # Open a json writer, and use the j
    # son.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
make_json(csvFilePath, jsonFilePath)
