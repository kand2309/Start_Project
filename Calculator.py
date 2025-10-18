print('\t\nДобро пожаловать в простой калькукулятор.')
print("""\t\nДоступные операции:
·Сложение (+)
·Вычетание (-)
·Умножение (*)
·Деление (/)
""")

num_1 = float(input('\nВведите первое число:'))
operator = input('Введите оператор (+, -, *, /):')
num_2 = float(input('Введите второе число:'))

if operator == "+":
    result = num_1 + num_2
    print(f"{num_1} {operator} {num_2} = {result}" )

elif operator == "-":
    result = num_1 - num_2
    print(f"{num_1} {operator} {num_2} = {result}" )

elif operator == "*":
    result = num_1 * num_2
    print(f"{num_1} {operator} {num_2} = {result}" )
    
elif operator == "/":
    result = num_1 / num_2
    print(f"{num_1} {operator} {num_2} = {result}" )
else:
    print("Ошибка!")
