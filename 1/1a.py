output = 0

with open('1/input.txt', 'r') as myfile:
    for line in myfile.readlines():
        operator = line[0]
        num = int(line[1:])

        if operator == "+":
            output += num
        else:
            output -= num

print(output)
