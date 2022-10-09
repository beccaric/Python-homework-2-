#Python Homework: Session 2 - 09 October 

#HLT 1: Times Tables - For Loop

num=1
for FourTimesTable in range (4,49,4):
  print(num, "x 4 = ", FourTimesTable)
  num=num+1


#HLT 2: Going Loopy
myname=input(("Please enter your name :"))
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total += num
    print("The total is",total,)
  

#HLT 3: Comparison/Logical Operators 
myname=input(("Please enter your name :"))
colour=(input("Please enter your favourite colour:"))
if colour == "red" or colour == "RED" or colour == "Red":
  print("I like Red too!")
else:
  print("I don't like Pink, I prefer Red!")
