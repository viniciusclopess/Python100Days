audiction = {}
def insert_dict(name, bid):
    audiction[name] = bid

while True:
    name = input("What is your name?\n-> ")
    bid = float(input("What is your bid?\n-> "))
    insert_dict(name, bid)
    other = input("There is any other participant? ('Y' for Yes, 'N' for No)\n-> ").upper()
    if other == "Y":
        continue
    else:
        break
