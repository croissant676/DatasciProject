import csv
import json

json_file = open('C:\\Users\\crois\\Downloads\\steamdb.json', 'r', encoding='utf-8')
json_data = json.load(json_file)

csv_file = open('data.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)

first = True
csv_writer.writerow(['steam_id',
                     'name',
                     'steam_rating',
                     'metacritic_rating',
                     'igdb_rating',
                     'metacritic_score',
                     'owner_count',
                     'full_price',
                     'achievements',
                     'is_windows',
                     'language_count',
                     'tag_count',
                     'is_multiplayer'
                     ])
for game in json_data:
    data_list = [
        game['sid'],
        game['name'],
        game['store_uscore'],
        game['meta_uscore'],
        game['igdb_uscore'],
        game['meta_score'],
        game['stsp_owners'],
        game['full_price'],
        game['achievements']
    ]
    if any(data is None for data in data_list):
        continue
    platforms = game['platforms']
    if platforms is None:
        continue
    if 'windows' in map(lambda x: x.lower(), platforms):
        data_list.append('T')
    else:
        data_list.append('F')
    languages = game['languages']
    if languages is None:
        continue
    data_list.append(len(languages.split(',')))
    tags = game['tags']
    if tags is None:
        continue
    tags = tags.split(',')
    data_list.append(len(tags))
    if 'multiplayer' in map(lambda x: x.lower(), tags):
        data_list.append('T')
    else:
        data_list.append('F')
    print(data_list)
    csv_writer.writerow(data_list)

csv_file.close()
