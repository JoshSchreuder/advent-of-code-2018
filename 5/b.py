def strip_react(polymer_fn):
    polymer = polymer_fn()
    result = {}

    letters = list(set(polymer.lower()))

    for letter in letters:
        stripped = polymer.replace(letter, "").replace(letter.upper(), "")
        result[letter] = react(stripped)

    return min(result.values())


def react(stripped):
    i = 0

    while i < len(stripped) - 1:
        if stripped[i].upper() == stripped[i+1].upper() and stripped[i] != stripped[i+1]:
            stripped = stripped[:i] + stripped[i+2:]
            if i > 2:
                i -= 2
            elif i >= 1:
                i -= 1
        else:
            i += 1

    return len(stripped)
