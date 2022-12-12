with open('input.txt', 'r') as file:
    lines = file.readlines()
    calories = []
    last = 0
    for line in lines:
        if line.strip() == "":
            calories.append(last)
            last = 0
        else:
            last = last + int(line.strip())
    calories.sort(reverse=True)
    print(sum(calories[:3]))
