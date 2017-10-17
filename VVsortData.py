#VermontVelo Project: Sorting Dataset
#Shannon Ovitt, Craig Calhoun

#demo code for csv
# import csv
#
# with open(<datafile>, 'wb') as data_file:
#     w = csv.writer(data_file, deliminer= ',')

import json

#object
data = {}
data['route'] = {
    'path': [],
    'parking': [],
    'length': [],
    'hazards': [],
    'lodging': [],
    'food': [],
    'closure': [],
    'path': [],
    'county': [],
    'bike_shops': [],
    'scenic': [],
    'route_start': [],
    'route_end': [],
    'elevation': [],
    'elevation_change': []
    }


with open('VVtest.json') as data_file:
    d = json.load(data_file)
    for x in d['route']['coordinates']:
        #data['route']['path'].append( d['route']['coordinates']) appends whole 'coordinates' array as one unit.
        data['route']['path'].append(x)
    #print(d['route']['coordinates'])

#write to json file.
with open('VVouttest.json', 'w') as output_file:
    json.dump(data, output_file, indent=4, sort_keys=True) #sort_keys sorts keys alphabetically
