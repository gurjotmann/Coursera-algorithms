import sys
def car_fuelling_recursioin(location,distance,tank,stops):
    if location + tank >=distance:
        return 0
    if len(stops)==0 or (stops[0]-location)>tank:
        return float('inf')
    last_stop = location
    while len(stops)!=0 and (stops[0]-location)<=tank:
        last_stop=stops[0]
        stops.pop(0)
    return 1 + car_fuelling_recursioin(last_stop,distance,tank,stops)

if __name__ == '__main__':
    d, tank, _, *stops = map(int, sys.stdin.read().split())
    x=car_fuelling_recursioin(0,d,tank,stops)
    if x==float('inf'):
       print(-1)
    else:
       print(x) 
