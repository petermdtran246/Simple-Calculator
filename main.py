print('Menu\n')
print("1. Add\n2. Sub\n3. Mul\n4. Div")
option = int(input('Enter your choice: '))
a, b = map(int, input('Enter 2 numbers: ').split())
match option:
    case 1: c = a + b
    case 2: c = a - b
    case 3: c = a * b
    case 4: c = a / b
print(f'Result is: {c}\n')



