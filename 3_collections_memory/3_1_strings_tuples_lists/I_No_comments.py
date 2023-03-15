str_list = []
while (s := input()) != '':
    str_list.append(s)

for el in str_list:
    if el.startswith('#'):
        continue
    pos = el.find('#')
    if pos != -1:
        print(el[:pos])
    else:
        print(el)
