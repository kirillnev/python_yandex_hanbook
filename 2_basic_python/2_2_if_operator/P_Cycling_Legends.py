v = {
    'Петя': int(input()),
    'Вася': int(input()),
    'Толя': int(input()),
}

sorted_v = sorted(v.items(), key=lambda x: x[1], reverse=True)

print(sorted_v[0][0].center(24))
print(sorted_v[1][0].center(8))
print(' ' * 15, sorted_v[2][0].center(8))
print('   II      I      III   ')
