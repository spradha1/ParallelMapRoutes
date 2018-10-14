import googlemaps
from datetime import datetime
import sys
from multiprocessing import Process
from locationspy import *
import time

def get_routes(spots):
    gmaps = googlemaps.Client(key='AIzaSyBQ6W3-fmXqMq3-llcbdiWKz-Ty0Ld9dIc')
    now = datetime.now()
    for i in range(0, len(spots)):
        try:
            directions_result = gmaps.directions("University of New Orleans",
                                                spots[i],
                                                mode="driving",
                                                departure_time=now)
            print spots[i] + ', ' + directions_result[0]['legs'][0]['distance']['text'] + ', ' + directions_result[0]['legs'][0]['duration']['text']
        except:
            print spots[i] + ': NOT FOUND'

if __name__ == '__main__' : 
    if len(sys.argv) < 2:
        print "Error: Number of threads/processes absent"
        sys.exit()
    elif int(sys.argv[1]) <= 0:
        print "Negative number of processes given"
        sys.exit()
    else:
        n = int(sys.argv[1])

    cases = len(locations)
    divvy = cases/n
    extras = cases%n
    jobs = []

    begin = time.time()

    for prcs in range(0, n):
        start = prcs*divvy + prcs
        if prcs > extras:
            start -= (prcs - extras)
        end = start + divvy
        if prcs < extras:
            end += 1

        p = Process(target=get_routes, args=(locations[start:end],))
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()

    end = time.time()
    print 'Time: ' + str(end-begin) + ' seconds'