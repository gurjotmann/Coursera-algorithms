class Animal(object):
    def __init__(self,age):
        self.years=age
        self.name=None
    def get_age(self):
        return self.years
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
        return "anmimal:"+str(self.name)+":"+str(self.age)
A=Animal(5)
y= A.get_age()
A.set_name("cat")
A.set_age(12)
A.set_name('dog')
print(A,y)