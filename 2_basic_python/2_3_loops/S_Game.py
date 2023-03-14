minimal_number = 0
maximum_number = 1001

user = ''

while user != 'Угадал!':
    number = (minimal_number + maximum_number) // 2
    print(number)
    user = input()
    if user == 'Меньше':
        maximum_number = number
    elif user == 'Больше':
        minimal_number = number
