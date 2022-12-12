def codex(c):
    if c.isupper():
        n = ord(c) - 38
    else:
        n = ord(c) - ord('a') + 1
    return int(n)


with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    counter = 0
    rucksacks = ["", "", ""]
    for rucksack in lines:
        rucksacks[counter % 3] = rucksack.strip()
        counter += 1
        if counter % 3 == 0:
            for i in rucksacks[0]:
                if i in rucksacks[1] and i in rucksacks[2]:
                    result += codex(i)
                    break
    print(result)
