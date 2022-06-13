class Student:
    def __init__(self, name, age, class_="Student"):
        self.name=name
        self.age=age
        self.class_=class_
    def score(self,test1,test2,test3):
        print((test1+test2+test3)/3)
        return (test1+test2+test3)/3


zake = Student('zake','30')

score=zake.score(80,43,39)
print(getattr(zake,"class_"))
print(zake.__dict__)

