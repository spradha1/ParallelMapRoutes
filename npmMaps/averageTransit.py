import sys

if __name__ == '__main__' :
    f = open(sys.argv[1], 'r')
    distance = 0
    duration = 0
    for line in f:
        values = line.rstrip().split()
        distance += float(values[0])
        duration += float(values[1])
    print "Miles covered on average in a minute: " + str(distance*60/duration)