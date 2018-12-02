def checksum(getBoxesFunc):
    boxes = getBoxesFunc()
    twos = 0
    threes = 0

    for box in boxes:
        foundTwo = False
        foundThree = False
        for uniq in set(list(box)):
            count = box.count(uniq)
            if count == 2 and not foundTwo:
                twos += 1
                foundTwo = True
            elif count == 3 and not foundThree:
                threes += 1
                foundThree = True

    return twos * threes
