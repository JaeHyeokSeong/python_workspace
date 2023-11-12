# https://teddylee777.github.io/visualization/folium/

import json
import requests
import folium
from geopy.geocoders import Nominatim
import googlemaps


def get_current_location():
    request = requests.get('http://www.geoplugin.net/json.gp')

    if request.status_code != 200:
        print('failed to get a current location')
    else:
        location = json.loads(request.text)
        current_location = {
            'latitude': location['geoplugin_latitude'],
            'longitude': location['geoplugin_longitude']
        }
        return current_location


def get_address(latitude, longitude):
    geo = Nominatim(user_agent='South Korea')
    address_coordinate = f'{latitude}, {longitude}'
    return geo.reverse(address_coordinate)


def visualize_address(latitude, longitude, file_name):
    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude]).add_to(m)
    m.save(file_name)


if __name__ == '__main__':
    current_location = get_current_location()
    visualize_address(
        current_location['latitude'],
        current_location['longitude'],
        'current_location_map.html'
    )

