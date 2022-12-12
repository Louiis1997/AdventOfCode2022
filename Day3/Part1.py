def codex(c):
    if c.isupper():
        n = ord(c) - 38
    else:
        n = ord(c) - ord('a') + 1
    return int(n)


with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for rucksack in lines:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        for i in first_compartment:
            if i in second_compartment:
                result += codex(i)
                break
    print(result)

