import os

bid_dict = {}
bid_finished = False

def clear():
  os.system('cls')

while not bid_finished :
  name = input("What is your name? : ")
  bid = int(input("What is your bid? : $"))
  other_bidders = input("Are there any other bidders? Type 'yes'or 'no'.")
  bid_dict[name] = bid
  
  if other_bidders == "no":
    bid_finished = True
  elif other_bidders == "yes":
    clear()

highest_bid = 0
for bidder in bid_dict:
  bid_amount = bid_dict[bidder]
  if bid_amount > highest_bid :
    highest_bid = bid_amount
    winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")
