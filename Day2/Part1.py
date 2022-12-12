Dict = {"X": 1, "Y": 2, "Z": 3}


def match(round, result):
    match round:
        case "A X":
            result += Dict["X"] + 3
        case "A Y":
            result += Dict["Y"] + 6
        case "A Z":
            result += Dict["Z"] + 0
        case "B X":
            result += Dict["X"] + 0
        case "B Y":
            result += Dict["Y"] + 3
        case "B Z":
            result += Dict["Z"] + 6
        case "C X":
            result += Dict["X"] + 6
        case "C Y":
            result += Dict["Y"] + 0
        case "C Z":
            result += Dict["Z"] + 3
    return result


with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for line in lines:
        result = match(line.strip(), result)
    print(result)
