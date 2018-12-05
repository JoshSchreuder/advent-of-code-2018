def react(polymer_fn):
    polymer = polymer_fn()

    i = 0

    while i < len(polymer) - 1:
        if polymer[i].upper() == polymer[i+1].upper() and polymer[i] != polymer[i+1]:
            polymer = polymer[:i] + polymer[i+2:]
            if i > 2:
                i -= 2
            elif i >= 1:
                i -= 1
        else:
            i += 1

    return len(polymer)
