def move(nb_time, from_stack, to_stack):
    for i in range(nb_time):
        to_stack.insert(len(to_stack)-i, from_stack.pop())


with open('input.txt', 'r') as file:
    lines = file.readlines()
    moveStarted = False
    cranes = dict()
    result = ""
    for line in lines:
        if not moveStarted:
            if line.strip() == "1   2   3   4   5   6   7   8   9":
                moveStarted = True
            else:
                for i in range(1, len(line), 4):
                    if line[i] != " ":
                        index = i // 4 + 1
                        if index not in cranes:
                            cranes[index] = []
                        cranes[index].insert(0, line[i])
        else:
            if line.strip() == "":
                continue
            split = line.strip().split()
            move(int(split[1]), cranes[int(split[3])], cranes[int(split[5])])
    for i in range(1, 10):
        result += (cranes[i][-1])
    print(result)
