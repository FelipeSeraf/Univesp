class Pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()

    def empty(self):
        return not len(self.data) > 0

    def conver(self, decimal):
