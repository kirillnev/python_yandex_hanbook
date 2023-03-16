translite_tbl = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
                 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
                 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E',
                 'Ю': 'Iu', 'Я': 'Ia', 'Ь': '', 'Ъ': ''}
tmp = {}
for k, e in translite_tbl.items():
    tmp[k.lower()] = e.lower()
translite_tbl = translite_tbl | tmp
text = input()
text_translite = ''
for ch in text:
    text_translite += translite_tbl[ch] if ch in translite_tbl else ch
print(text_translite)
