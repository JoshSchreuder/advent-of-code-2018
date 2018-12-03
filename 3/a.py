import re


def overlap(load_claims):
    claims = list(map(parseClaim, load_claims()))
    taken = {}

    for claim in claims:
        for x in range(0, claim["xSize"]):
            for y in range(0, claim["ySize"]):
                coord = str(x + claim["x"]) + "," + str(y + claim["y"])
                if coord in taken:
                    taken[coord] += 1
                else:
                    taken[coord] = 1

    return len(dict((k, v) for k, v in taken.items() if v >= 2))


def parseClaim(claim):
    parsed = re.search('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim)

    return dict(
        claimNum=int(parsed.group(1)),
        x=int(parsed.group(2)),
        y=int(parsed.group(3)),
        xSize=int(parsed.group(4)),
        ySize=int(parsed.group(5))
    )
