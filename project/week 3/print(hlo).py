# python3
import sys
def compute_min_refills(distance, tank, stops):
    location = 0
    last_location=0
    n=0
    if tank<stops[0]:
        return -1
    while (location+tank)<distance:
        while (abs(stops[0]-location))<=tank :
            if len(stops)==1:
                if (distance-stops[0])>tank:
                    return -1
            if (stops[0]-location)>tank:
                return -1
            last_location=stops[0]
            stops.remove(stops[0])
            if len(stops)==0:
                break
        location=last_location
        n+=1
    return n
d=10
t=3
stops=[1,2,5,6]
print(compute_min_refills(d,t,stops))