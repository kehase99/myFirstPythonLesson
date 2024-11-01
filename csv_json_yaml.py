import json
import yaml
import csv

print("---------------------------------------")
with open('test_json_file.json', 'r') as data_json_file:
     data = json.load(data_json_file)
     print(data)



write_json_data = [
    {
        "name": "Joe",
        "age": 35,
        "city": "Berlin"
    },
    {
        "name": "Michel",
        "age": 45,
        "city": "Paris"
    }
]

with open('new_data.json', 'w') as new_data_json_file:
    json.dump(write_json_data, new_data_json_file)

print("-----------------------------------------")

write_yaml_data = [
    {
        "name": "Joe",
        "age": 35,
        "city": "Berlin"
    },
    {
        "name": "Michel",
        "age": 45,
        "city": "Paris"
    }
]

with open('data_yaml.yml', 'w') as data_yaml_file:
    yaml.dump(write_yaml_data, data_yaml_file)

with open('data_yaml.yml', 'r') as data_read_yaml_file:
    data = yaml.safe_load(data_read_yaml_file)
    print(data)

print("--------------------------------------------")

with open('test_csv_file.csv', 'r') as data_csv_file:
    data_reader = csv.reader(data_csv_file)

    for row in data_reader:
        print(row)

csv_data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', '30', 'New York'],
    ['Jane', '25', 'London']
]

with open('new_csv_data.csv', 'w') as write_csv_data_file:
    write_csv = csv.writer(write_csv_data_file)
    write_csv.writerows(csv_data_to_write)