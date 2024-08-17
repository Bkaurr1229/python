print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#code with use of count and lower
name= name1+name2
lover_name=name.lower()
t= lover_name.count("t")
r= lover_name.count("r")
u= lover_name.count("u")
e= lover_name.count("e")
first_digit= t + r + u + e 

l= lover_name.count("l")
o= lover_name.count("o")
v= lover_name.count("v")
e= lover_name.count("e")
second_digit= l+o+v+e

score= int( str(first_digit) +str(second_digit))
if(score<10) or (score>90):
 print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40) and (score<=50):
 print(f"Your score is {score}, you are alright together.")
else:
 print(f"Your score is {score}.")