unit= str(input("Gallons or litres? "))
x=int(input("Enter the capacity of first jug in litres: "))
y=int(input("Enter the capacity of second jug in litres: "))

gsPreference=int(input("Both jugs: (0) || First jug (1) || Second jug (2): "))
goalStates=set()
X,Y=x+1, y+1

if gsPreference==0:
    while X>x or Y>y:
        X,Y=[int(i) for i in input("\nEnter goal state capacity of both the jugs separated by space: ").split(' ')]
        if X>x or Y>y:
            print("Warning: Goal state capacity cannot be greater than capacity of the jugs.")
    goalStates.add((X, Y))
elif gsPreference==1:
    while X>x:
        X=int(input("\nEnter the goal state capacity in 1st jug: "))
        if X>x:
            print("Warning: Goal state capacity cannot be greater than capacity of the jugs.")
    for i in range(0, y+1, 1):
        goalStates.add((X, i)) 
elif gsPreference==2:
    while Y>y:
        Y=int(input("\nEnter the goal state capacity in 2nd jug: "))
        if Y>y:
            print("Warning: Goal state capacity cannot be greater than capacity of the jugs.")
    for i in range(0, x+1, 1):
        goalStates.add((i, Y))

print("Goal states as a set of tuples:",goalStates)

initialState=[(0,0)]