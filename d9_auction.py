import os 
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-"*60)

audiction = {}
def insert_dict(name, bid):
    audiction[name] = bid
    print(f"The bid {bid} of {name} was added!")

def highest_bid():
    max_bid = 0
    winner = "" 
    for name, bid in audiction.items():
        if bid > max_bid:
            max_bid = bid
            winner = name
    print(f"The winner of the audiction is {winner} with ${max_bid}!! ")

while True:
    name = input("What is your name?\n-> ")
    bid = float(input("What is your bid?\n-> "))
    insert_dict(name, bid)
    other = input("There is any other participant? ('Y' for Yes, 'N' for No)\n-> ").upper()
    time.sleep(1)
    limpar_terminal()
    
    if other == "Y":
        continue
    elif other == "N":
        limpar_terminal()
        highest_bid()
        break
    else:
        print("Invalid input")