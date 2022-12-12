with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for section in lines:
        Elf_section = section.strip().split(',')
        first_elf = Elf_section[0].split('-')
        second_elf = Elf_section[1].split('-')
        if int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1]) \
                or int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1]):
            result += 1
    print(result)
