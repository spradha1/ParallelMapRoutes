import googlemaps
from datetime import datetime
import sys
from locationspy import *
import threading
from multiprocessing import Process
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, spots):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.spots = spots
    def run(self):
        get_routes(self.spots)

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
    elif int(sys.argv[1]) <= 0 or int(sys.argv[1])%2 == 1:
        print "Only even positive numbers accepted for uniform division between threads and processes"
        sys.exit()
    else:
        n = int(sys.argv[1])

    cases = len(locations)
    divvy = cases/n
    jobs = []
    extras = cases%n

    begin = time.time()

    for prcs in range(0, n):
        start = prcs*divvy + prcs
        if prcs > extras:
            start -= (prcs - extras)
        end = start + divvy
        if prcs < extras:
            end += 1
            
        if prcs < n/2:
            p = Process(target=get_routes, args=(locations[start:end],))
            jobs.append(p)
            p.start()    
        else:
            name = "Thread #" + str(prcs) 
            thread1 = myThread(prcs, name, locations[start:end])
            jobs.append(thread1)
            thread1.start()
    
    for j in jobs:
        j.join()

    end = time.time()
    print 'Time: ' + str(end-begin) + ' seconds'