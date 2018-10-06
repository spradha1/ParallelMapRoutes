import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBQ6W3-fmXqMq3-llcbdiWKz-Ty0Ld9dIc')
now = datetime.now()
a = [1,2,3,4,5,6,7]
print 35%6
try:
    directions_result = gmaps.directions("University of New Orleans",
                                            "76786kjk",
                                            mode="driving",
                                            departure_time=now)
except:                                   
    print 'NOT FOUND'