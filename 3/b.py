import re
from collections import Counter


def not_overlap(load_claims):
    claims = list(map(parseClaim, load_claims()))
    patches = getPatches(claims)

    coords = list(x for v in patches.values() for x in v)
    counter = Counter(coords)

    return next((k, v) for k, v in patches.items() if all(
        counter[coord] == 1 for coord in v))[0]


def getPatches(claims):
    patches = {}
    for claim in claims:
        patches[claim["claimNum"]] = []
        for x in range(0, claim["xSize"]):
            for y in range(0, claim["ySize"]):
                coord = str(x + claim["x"]) + "," + str(y + claim["y"])
                patches[claim["claimNum"]].append(coord)

    return patches


def parseClaim(claim):
    parsed = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)

    return dict(
        claimNum=int(parsed.group(1)),
        x=int(parsed.group(2)),
        y=int(parsed.group(3)),
        xSize=int(parsed.group(4)),
        ySize=int(parsed.group(5))
    )
