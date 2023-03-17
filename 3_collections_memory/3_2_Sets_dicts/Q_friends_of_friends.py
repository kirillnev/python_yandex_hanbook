persons = {}
while (s := input()) != '':
    s = s.split()
    # print(friends.get(s[0], []))
    persons[s[0]] = persons.get(s[0], []) + [s[1]]
    persons[s[1]] = persons.get(s[1], []) + [s[0]]

friends_2 = {}
for name, friends in persons.items():
    friends_2[name] = []
    for person in friends:
        friends_2[name] += persons[person]
    friends_2[name] = set(friends_2[name])
    friends_2[name].discard(name)

friends_2 = dict(sorted(friends_2.items(), key=lambda x: x[0]))
for name, friends in friends_2.items():
    s = []
    for friend in friends:
        if friend not in persons[name]:
            s.append(friend)
    s.sort()
    print(f'{name}: {", ".join(s)}')
