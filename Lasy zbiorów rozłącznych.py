class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y: return #Już są połączone

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
