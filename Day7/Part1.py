with open('input.txt', 'r') as file:
    lines = file.readlines()
    dico = dict()
    current = ""
    result = 0
    for line in lines:
        cmd = line.split(' ')
        if cmd[0] == '$':
            match cmd[1]:
                case 'cd':
                    current = cmd[2].strip()
        else:
            if cmd[0] != 'dir':
                dico[current] = cmd[0] if current not in dico else int(dico[current]) + int(cmd[0])
    print(dico)
    #for i in dico:
     #   result += int(dico[i]) if int(dico[i]) <= 100000 else 0
    #print(result)

