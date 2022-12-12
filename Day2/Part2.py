Dict = {"X": 0, "Y": 3, "Z": 6}


def match(round, result):
    match round:
        case "A X":
            result += 3 + Dict["X"]
        case "A Y":
            result += 1 + Dict["Y"]
        case "A Z":
            result += 2 + Dict["Z"]
        case "B X":
            result += 1 + Dict["X"]
        case "B Y":
            result += 2 + Dict["Y"]
        case "B Z":
            result += 3 + Dict["Z"]
        case "C X":
            result += 2 + Dict["X"]
        case "C Y":
            result += 3 + Dict["Y"]
        case "C Z":
            result += 1 + Dict["Z"]
    return result


with open('input.txt', 'r') as file:
    lines = file.readlines()
    result = 0
    for line in lines:
        result = match(line.strip(), result)
    print(result)
