
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1-n2

def multipy(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

dict_operation ={"+": add, "-":subtract ,"*":multipy,  "/":divide}
def calculator():
  #for decimal calculating add float
  number=int(input("What is your first number?"))

  for symbol in dict_operation:
    print(symbol)

  should_continue = True
  while should_continue :
    operation= input("Pick an operation")
    number2 =int(input("What is your second number?"))
    calculation_function = dict_operation[operation]
    answer = calculation_function(number,number2)

    print(f"{number} {operation} {number2}= {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator:  ") == "y":
      number = answer 
    else:
      should_continue = False

calculator()