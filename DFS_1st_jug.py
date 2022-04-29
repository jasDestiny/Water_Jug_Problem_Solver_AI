from collections import deque

def DFS(a, b, target):
    m={}
    isSolvable=False
    path=[]
    
    q=deque()
    q.append((0,0))
    while len(q)>0:
        u=q.popleft()
        # if ((u[0], u[1]) in m):
        #     continue
        if ((u[0], u[1]) in m) or (u[0]>a or u[1]>b or u[0]<0 or u[1]<0):
            continue
        
        path.append([u[0], u[1]])
        m[(u[0], u[1])] = 1
        if (u[0] == target or u[1] == target):
            isSolvable = True
            
            if (u[0] == target):
                if (u[1] != 0):
                    path.append([u[0], 0])
            
            else:
                if (u[0] != 0):
                    path.append([0, u[1]])
            
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",",path[i][1],")")
                if path[i][0]==target:
                    return
                print("    |")
                print("    v")
            break
        q.append([u[0], b])
        q.append([a, u[1]])
        
        for ap in range(max(a,b)+1):
            c = u[0] + ap
            d = u[1] - ap

            if (c == a or (d == 0 and d >= 0)):
               q.append([c, d])
            
            c = u[0] - ap
            d = u[1] + ap
            
            if ((c == 0 and c >= 0) or d == b):
                q.append([c, d])
        q.append([a, 0])
        q.append([0, b])
    if (not isSolvable):
        return "Solution is not possible for the given input for the given input."

jug1= int(input("Enter the capacity of the first water jug in litres: "))
jug2= int(input("Enter the capapcity of the second water jug in litres: "))
target= int(input("Enter the target capacity: "))
DFS(jug1, jug2, target)
print("Goal state is reached")