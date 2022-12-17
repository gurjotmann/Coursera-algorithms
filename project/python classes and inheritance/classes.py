class coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,another):
        x_diff=(self.x-another.x)**2
        y_diff=(self.y-another.y)**2
        return (x_diff+y_diff)**0.5
    def __str__(self):
        return "<"+str(self.x)+ ","+str(self.y)+">"
firstpoint=coordinate(5,6)
another=coordinate(2,3)
hello=[]
print(another.distance(firstpoint))
print(firstpoint)
print(type(firstpoint))
print(coordinate)
print(isinstance(firstpoint,coordinate))
print(type(hello))