class predict1():
    def __init__(self, x = None):
        self.x = x
    def getPredict(self, x):
        self.x = x
        self.y = x * 2
        print('Predict Result :', self.y)

class predict2():
    def __init__(self, x = None):
        self.x = x
    def getPredict(self, x):
        self.x = x
        self.y = (x * -0.5) + (x + 2)
        print('Predict Result :', self.y)

class predict3():
    def __init__(self, x1 = None, x2 = None):
        self.x1 = x1
        self.x2 = x2
    def getPredict(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.y = self.x1 + self.x2
        print('Predict Result :', self.y)

class predict4():
    def __init__(self, x1 = None, x2 = None):
        self.x1 = x1
        self.x2 = x2
    def getPredict(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        if self.x2 > 3:
            self.y = self.x1 * 0 + self.x2 * 3
        else:
            self.y = self.x1 * 0.25 + self.x2 * 2.75
        print('Predict Result :', self.y)
