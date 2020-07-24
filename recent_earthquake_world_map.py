#!/usr/bin/env python3

import json
import requests
from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Get earthquake data
# https://earthquake.usgs.gov/earthquakes/feed/
data = requests.get('https://earthquake.usgs.gov/earthquakes/' +
                    'feed/v1.0/summary/1.0_week.geojson').content
all_eq_data = json.loads(data)

# Read from a file
# filename = 'data/1.0_week.geojson'
# with open(data) as f:
#     all_eq_data = json.load(f)

# Write to a readable fisle
# readable_file = 'data/readable_1.0_day.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

source = all_eq_data['metadata']['title']
amount = all_eq_data['metadata']['count']
timestamp = int(all_eq_data['metadata']['generated'])/1000
gen_date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %I:%M:%S")
all_eq_dicts = all_eq_data['features']
title = f'Global Earthquakes<br /><sup>{source}, count: {amount}, ' + \
        f'generated: {gen_date}</sup>'

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    # 'projection': 'natural earth',
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Rainbow',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
