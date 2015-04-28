class A(object):
    """docstring for A"""
    def __init__(self, v):
        self.v = v

    def add(self, b):
        return self.v + b.v

    def __str__(self):
        return str(self.v)

a = A(10)
b = A(20)
print a.add(b)
print A.add(a, b)
