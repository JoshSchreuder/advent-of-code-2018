def checkSeen(output, seen):
    if output in seen:
        return True

    seen.append(output)
    return False


def getFrequencies(loadFrequencies):
    output = 0
    seen = [output]

    while True:
        for line in loadFrequencies():
            operator = line[0]
            num = int(line[1:])

            if operator == "+":
                output += num
            else:
                output -= num

            if checkSeen(output, seen):
                return output
