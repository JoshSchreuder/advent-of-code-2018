def similar(getBoxesFunc):
    boxes = getBoxesFunc()

    for i in range(0, len(boxes)):
        for j in range(i, len(boxes)):
            [matchCount, nonMatching] = overlap(boxes[i], boxes[j])

            if matchCount == (len(boxes[i]) - 1):
                return boxes[i].replace(nonMatching, "")

    return ""


def overlap(string1, string2):
    count = 0
    nonMatching = ""
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            count = count + 1
        else:
            nonMatching = string1[i]
    return [count, nonMatching]
