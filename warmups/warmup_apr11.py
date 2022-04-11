#!/usr/bin/python3

import requests
import datetime
import reverse_geocoder as rg

url = 'http://api.open-notify.org/iss-now.json'

def main():

    items = requests.get(f'{url}')
    items = items.json()

    latitude = items['iss_position']['latitude']
    longitude = items['iss_position']['longitude']

    location = rg.search((latitude, longitude))[0]

    print('CURRENT LOCATION OF THE ISS:')    
    epoch_time = items['timestamp']
    date_time = datetime.datetime.fromtimestamp( epoch_time )
    print(date_time)

    print(f"Lon: {longitude}")
    print(f"Lat: {latitude}")
    if location['admin1'] == '' or location['admin1'] == None:
        print(f"{location['name']}, {location['cc']}")
    else:
        print(f"{location['name']}, {location['admin1']}, {location['cc']}")

if __name__ == '__main__':
    main()
