elf_number = input()
gnome_number = input()
human_number = input()

for i in range(len(elf_number)):
    if elf_number[i] == gnome_number[i] == human_number[i]:
        print(elf_number[i])
        break

