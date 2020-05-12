class classname():
    def __init__(self, value = 'Jane'):
        self.thing = value
        self.thing2 = value + ' fff'
    def func1(self):
        return self.thing
    def func2(self):
        return self.thing2


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def innerPrint(self, infor):
        print(infor, self.x, self.y)
