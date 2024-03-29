import sys
def get_optimal_value(capacity, weights, values):
    value=0
    values = [m/n for m,n in zip(values,weights)]
    while capacity>0:
       y= max(values)
       x= weights[values.index(y)]
       if x<=capacity:
           capacity-=x
           value+= (x*y)
           if len(weights)==1:
               return value
           values.remove(y)
           weights.remove(x)
       elif  x>capacity:
           return value+(capacity*y)
    return value
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


