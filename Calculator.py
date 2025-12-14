print('\t\nWelcome to the Simple Calculator.')
print("""\t\nAvailable operations:
·Addition (+)
·Subtraction (-)
·Multiplication (*)
·Division (/)
""")

num_1 = float(input('\nEnter the first number: '))
operator = input('Enter the operator (+, -, *, /): ')
num_2 = float(input('Enter the second number: '))

if operator == "+":
    result = num_1 + num_2
    print(f"{num_1} {operator} {num_2} = {result}")

elif operator == "-":
    result = num_1 - num_2
    print(f"{num_1} {operator} {num_2} = {result}")

elif operator == "*":
    result = num_1 * num_2
    print(f"{num_1} {operator} {num_2} = {result}")
    
elif operator == "/":
    result = num_1 / num_2
    print(f"{num_1} {operator} {num_2} = {result}")
    
else:
    print("Error: Invalid operator!")
