import geojson

import parse as p

def create_map(data_file):
    # Define type of GeoJSON to create
    geo_map = {"type": "FeatureCollection"}

    # Define empty list to collect each point to graph
    item_list = []

    # Iterate over data to create GeoJSON document
    # Use enumerate() to get the line as well as the index
    # which is the line number
    for index, line in enumerate(data_file)

        # Skip any zero coordinates
        if line['X'] == "0" or line["Y"] == "0":
            continue

        # Setup a new dictionary for each iteration
        data = {}

        # Assign line items to appropriate GeoJSON fields
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # Add data dictionary to item_list
        item_list.append(data)

    # For each point in item_list, add it to dictionary
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # Once all data is parsed in GeoJSON write to a file
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)

if __name__ == "__main__":
    main()
