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
        Employee1.empCount += 1
    def displayCount(self):
        return print('Total Employee :', Employee1.empCount)
    def displayEmployee(self):
        return print('Name :', self.name, 'Salary :', self.salary)
    
class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
        self.dob = None

class Country():
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드 입니다.')


class Korea(Country):
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital
    def showName(self):
        print('Country Name is', self.name)


# k = Korea('korea', '5000', 'seoul')
# k.showName()
# k.show()



