print("Welcome to Python Calculator!")
running = True

def selected_operation(n1, op, n2):
    if op == '+':
        result = n1 + n2
        return print(f"{n1} + {n2} = {result}")

    elif op == '-':
        result = n1 - n2
        return print(f"{n1} - {n2} = {result}")

    elif op == '*':
        result = n1 * n2
        return print(f"{n1} * {n2} = {result}")

    elif op == '/':
        result = n1 / n2
        return print(f"{n1} / {n2} = {result}")
    else:
        print("Invalid operation!")

while running:
    first_number = float(input("Enter the first number: "))
    operation = input("""
+
-
*                                                          
/                  
Pick a operation: """)
    next_number = float(input("Enter the next number: "))
    selected_operation(first_number, operation, next_number)
    break # I just not want to continue from the last result. (Now)
