with open('input.txt', 'r') as file:
    lines = file.readlines()
    distinct_characters = 14
    result = 0
    for line in lines:
        for i in range(0, len(line)-distinct_characters):
            if line[i+1:i+distinct_characters].count(line[i]) == 0:
                for j in range(distinct_characters-1, 0, -1):
                    i += 1
                    if line[i+1:i+j].count(line[i]) == 0:
                        if j == 1:
                            result = i + 1
                            break
                    else:
                        break
    print(result)
