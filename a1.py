y = input("Enter Score: ")
x = int(y)
if x in range(0,0.59):
    print("F")
elif x in range(0.6,0.69):
    print("D")
elif x in range(0.7,0.79):
    print("C")
elif x in range(0.8,0.89):
    print("B")
elif x in range(0.9,1.0):
    print("A")
else:
    print("enter value between 0 and 1")
