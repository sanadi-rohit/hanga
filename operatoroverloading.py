#operator overloading in python
class husband:
    def __init__(self,salary):
        self.salary=salary
    def set_expense(self,expense):
        self.expense=expense
    def __add__(self, other):
        savh=self.salary-self.expense
        savw=other.salary-other.expense
        return savh+savw

class wife(husband):
    pass

h1=husband(30000)
h1.set_expense(15000)
w1=wife(20000)
w1.set_expense(15000)
savings=h1+w1
print(savings)


class add:
    def __init__(self,a=0,b=0,c=0):
        self.sum=a+b+c
    def __str__(self):
        return(f'{self.sum}')
a1=add(20,15,10)
print(a1)
a2=add(10,15)
print(a2)
a3=add(10)
print(a3)



