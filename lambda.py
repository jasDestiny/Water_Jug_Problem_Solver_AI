def get7(a, maxA, maxB):
        if sum(a)>=maxA and a[1]>0:
            return (maxA, a[1]-(maxA-a[0]))
        return a
    
def get8(a, maxA, maxB):
        if sum(a)>=maxB and a[0]>0:
            return (a[0]-(maxB-a[1]), maxB)
        return a
    
def get9(a, maxA, maxB):
        if sum(a)<=maxA and a[1]>0:
            return (sum(a), 0)
        return a
    
def get10(a, maxA, maxB):
        if sum(a)<=maxB and a[0]>0:
            return (0, sum(a))
        return a

l=[
    lambda a, maxA, maxB : (maxA, a[1]),
    lambda a, maxA, maxB : (a[0], maxB),
    lambda a, maxA, maxB : (0, a[1]),
    lambda a, maxA, maxB : (a[0], 0),
    
    lambda a, maxA, maxB : get7(a, maxA, maxB),
    lambda a, maxA, maxB : get8(a, maxA, maxB),
    
    lambda a, maxA, maxB : get9(a, maxA, maxB),
    lambda a, maxA, maxB : get10(a, maxA, maxB), 

    lambda a, maxA, maxB : (min(maxA, a[1]), min(maxB, a[0]))
]

for i in l:
    print(i((0, 0), 4, 3))