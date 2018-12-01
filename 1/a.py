def getFrequencies(loadFrequencies):
    output = 0
    for line in loadFrequencies():
        operator = line[0]
        num = int(line[1:])

        if operator == "+":
            output += num
        else:
            output -= num
    return output
