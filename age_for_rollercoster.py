print("Welcome to the rollersoater ")
height = int(input("what is your height in cm?"))

if height >= 120:
  print("you can ride the rollercoster")
  age = int(input("what is your age?"))
  bill=0
  if age <12:
    print("please pay 5")
    bill=5
  elif age>=18:
    print("please pay 7")
    bill=7
  else:
    print("please pay 12")
    bill=12
  want_photo=input("do you want a photo taken? y or n")
  if want_photo == "y":
   bill += 3
   print(f"your final bil is {bill}")
else:
  print("sorry, you have to grow taller before you can ride")