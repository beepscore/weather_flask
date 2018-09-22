import csv
import json
from weather_prop import WeatherProp

"""
Reads weather file seattle-data.csv, drops some fields, writes to .json
"""

# Define the header names so we can specify them when reading the CSV
fieldnames = (
    WeatherProp.STATION.value,
    WeatherProp.NAME.value,
    WeatherProp.DATE.value,
    WeatherProp.AWND.value,
    WeatherProp.PRCP.value,
    WeatherProp.SNOW.value,
    WeatherProp.SNWD.value,
    WeatherProp.TAVG.value,
    WeatherProp.TMAX.value,
    WeatherProp.TMIN.value,
    WeatherProp.WT01.value,
    WeatherProp.WT02.value,
    WeatherProp.WT03.value,
    WeatherProp.WT05.value,
    WeatherProp.WT08.value
)

# Open both files so we can interact with them
# Using the 'with' keyword lets us close the files automatically after these
# with blocks end and we're done writing and reading the files
with open('./data/seattle-data.csv', 'r') as csvfile:
    with open('./data/seattle-data.json', 'w') as jsonfile:
        # 'next' will simply skip over the header row in the csvfile
        next(csvfile)

        reader = csv.DictReader(csvfile, fieldnames)

        # This creates an empty dictionary to hold the final set of 
        # data that we'll eventually dump into the JSON file
        final_data = {}

        # Now we use the reader to iterate over all the rows of the CSV
        # (except for the header) and then keep the values we want 
        for row in reader:
            # We also restructure the data so that it exists as 
            # a set of date keys with the value as a dictionary of
            # different data elements from the CSV.
            final_data[row[WeatherProp.DATE.value]] = {
                WeatherProp.AWND.value: row[WeatherProp.AWND.value],
                WeatherProp.PRCP.value: row[WeatherProp.PRCP.value],
                WeatherProp.SNOW.value: row[WeatherProp.SNOW.value],
                WeatherProp.SNWD.value: row[WeatherProp.SNWD.value],
                WeatherProp.TAVG.value: row[WeatherProp.TAVG.value],
                WeatherProp.TMAX.value: row[WeatherProp.TMAX.value],
                WeatherProp.TMIN.value: row[WeatherProp.TMIN.value]
            }

        # Finally, we use the json library to output the final_data
        # dictionary to the jsonfile we opened earlier
        json.dump(final_data, jsonfile)
        # And then we write a final newline to the end of the file 
        # (this is just a best practice)
        jsonfile.write('\n')
