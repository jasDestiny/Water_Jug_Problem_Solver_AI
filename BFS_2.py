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
    
class tree:
    def __init__(self, node):
        self.val=node
        self.children=[]
        self.visited=set()
        self.l=[
            lambda a, maxA, maxB : (maxA, a[1]),
            lambda a, maxA, maxB : (a[0], maxB),
            lambda a, maxA, maxB : (0, a[1]),
            lambda a, maxA, maxB : (a[0], 0),
            
            lambda a, maxA, maxB : get7(a, maxA, maxB),
            lambda a, maxA, maxB : get8(a, maxA, maxB),
            
            lambda a, maxA, maxB : get9(a, maxA, maxB),
            lambda a, maxA, maxB : get10(a, maxA, maxB), 

            lambda a, maxA, maxB : (a[1], a[0]),
        ]
    
    def generateTree(self, goalState, maxA, maxB):
        visited={self.val:True}
        current=[self]
        x=0
        while True and x<10:
            x+=1
            nextCurrent=[]
            for hi in current:
                arr=[k(hi.val, maxA, maxB) for k in self.l]
                arr=set(arr)
                brr=[]
                for i in arr:
                    if i not in visited:
                        brr.append(i)
                        visited[i]=True
                
                arr=brr.copy()
                hi.children=[tree(hj) for hj in arr]
            
            for i in current:
                nextCurrent+=i.children
            nextCurrent=list(set(nextCurrent))
            current=nextCurrent.copy()

            for i in current:
                if i.val[1] == goalState:
                    return self
        return self
        
    def returnTreeLevelwise(self):
        solution=[[self.val]]
        parent=[self]
        
        x=-1
        while parent:
            child=[]
            childArr=[]
            for i in parent:
                for j in i.children:
                    if j!=[]:
                        child.append(j)
                        childArr.append(j.val)
                if childArr and childArr!=solution[-1]:
                    solution.append(childArr)
                else:
                    break
            parent=child.copy()
        return solution

    def printTreeLevelWise(self):
        print("\nSolution Tree")
        x=0
        for i in self.returnTreeLevelwise():
           print("Level:", x)
           print(i)
           x+=1
        return None

maxA=int(input("Enter the capacity of the first water jug in litres: "))
maxB=int(input("Enter the capacity of the second water jug in litres: "))
t=tree((0,0))
goalState=int(input("Enter goal number of litres of water in the second jug: "))
t.generateTree(goalState, maxA, maxB)
t.printTreeLevelWise()
