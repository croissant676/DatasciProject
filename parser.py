import csv
import json

json_file = open('C:\\Users\\crois\\Downloads\\steamdb.json', 'r', encoding='utf-8')
json_data = json.load(json_file)

csv_file = open('data.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)

first = True
for game in json_data:
    if first:
        header = game.keys()
        csv_writer.writerow(header)
        first = False
    csv_writer.writerow(game.values())

