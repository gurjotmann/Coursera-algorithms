def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
a,b=[int(x) for x in input().split()] #learnt taking multiple int values
def LCM(a,b):
    return (a*b)/GCD(a,b)
print(int(LCM(a,b)))