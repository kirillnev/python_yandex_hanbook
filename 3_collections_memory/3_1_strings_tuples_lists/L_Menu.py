days = int(input())
porridge = [
    'Манная',
    'Гречневая',
    'Пшённая',
    'Овсяная',
    'Рисовая',
]

print(*(porridge * (days // len(porridge) + 1))[:days], sep='\n')
