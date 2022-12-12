with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        for i in range(0, len(line)-3):
            if line[i] != line[i+1] and line[i] != line[i+2] and line[i] != line[i+3] \
                    and line[i+1] != line[i+2] and line[i+1] != line[i+3] and line[i+2] != line[i+3]:
                print(i+4)
                break
