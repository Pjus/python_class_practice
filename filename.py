class Classname:
    def __init__(self, value = 'Jane'):
        self.thing = value
        self.thing2 = value + ' fff'
    def func1(self):
        return self.thing
    def func2(self):
        return self.thing2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def innerPrint(self, infor):
        print(infor, self.x, self.y)


class Employee:
    def __init__(self, Name=None, Salary=None):
        self.name = Name
        self.salary = Salary
    def weeklySalary(self, name, Dailywage, Weekly):
        self.name = name
        self.daily = Dailywage
        self.week = Weekly
        return print('Name : {}, Salary : {}'.format(self.name, self.daily * self.week))

class Employee1:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee1.empCount += 1
    def displayCount(self):
        return print('Total Employee :',employee1.empCount)
    