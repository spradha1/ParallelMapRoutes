import googlemaps
from datetime import datetime
# from from_to import *
from datetime import datetime

def get_routes(a, b):
    gmaps = googlemaps.Client(key='YOUR_API_KEY')
    now = datetime.now()
    try:
        directions_result = gmaps.directions(a, b,
                                            mode="transit",
                                            departure_time=now)
        
        print a + ' - ' + b + ', ' + directions_result[0]['legs'][0]['distance']['text'] + ' ' + directions_result[0]['legs'][0]['duration']['text']
    except Exception as e:
        print e


if __name__ == '__main__' :
    get_routes("French Market Station", "Museum of Art, New Orleans")