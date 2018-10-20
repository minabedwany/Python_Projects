## Mina Bedwany  ID - 69543570

### API building

import json
import urllib.parse
import urllib.request

API_key = 'Im8njCC69lVCFAqMKr9DNdMLfac9VzIs'

Base_elevation_url = 'http://open.mapquestapi.com/elevation/v1/profile'
Base_directions_url = 'http://open.mapquestapi.com/directions/v2/route'

def build_directions_url(locations: list) -> str:

    for i in range(len(locations)):
        query_parameters = [
            ('key', API_key), ('from', locations[i]), ('to', locations[i+1]),
            ]
        return Base_directions_url + '?' + urllib.parse.urlencode(query_parameters)       


def build_elevation_url(locations: list) -> str:
    query_parameters = [
        ('key', API_key), ('shapeFormat', 'raw')
        ]
        #, ('latLngCollection', latlong(get_result(build_directions_url(locations))))
    url = Base_elevation_url + '?' + urllib.parse.urlencode(query_parameters)

    url += '&latLngCollection=' + latlong(get_result(build_directions_url(locations)))

    return url[:-1] 

def get_result(url: str) -> dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)        
    finally:
        if response != None:
            response.close()



def latlong(result: dict) -> str:
    lat_list = []
    lnglat = ''
    for item in result['route']['locations']:
        lnglat += str(item['latLng']['lat'])+',' + str(item['latLng']['lng']) + ','   
    return lnglat

        



