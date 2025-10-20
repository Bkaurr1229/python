
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 40,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"here is {change} your change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. money refunded ")
        return False

def resource_sufficient(order_ingredient,resources_item):
    for item in order_ingredient:
        if order_ingredient[item] >= resources_item[item]:  
          print(f"sorry there is not enough {item}")
          
        else:
            return True

def coins():
    one_ruppee=int(input("how many 1 ruppee coins:"))
    two_ruppee=int(input("how many 2 ruppee coins:"))
    five_ruppee=int(input("how many 5 ruppee coins:"))
    ten_ruppee=int(input("how many 10 ruppee coins:"))

    total = one_ruppee+(two_ruppee *2)+(five_ruppee*5)+(ten_ruppee*10)
    return total

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f" here is your {drink_name}. enjoy")

is_on=True

while is_on:
    choice= input("What would you like ? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:{profit}")
    else:
        drink = MENU[choice]
        print(resources)
        
        if resource_sufficient(drink["ingredients"],resources):

            payment = coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
        else:
            is_on = False