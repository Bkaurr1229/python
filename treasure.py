print("welcome to treaure island")
print("your mission is to find the treasure")
choice1=input("you're at a crossroad. where do you want to go? type'left' or 'right'\n")
if choice1=="left":
  choice2=input("you come to a lake. there is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim'to swim across\n")
  if choice2 =="wait":
    choice3=input("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow\n")

    if choice3=="yellow":
       print("you win")
else:
  print("game over")