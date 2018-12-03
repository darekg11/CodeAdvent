import re
from collections import defaultdict

def readLinesFromFile(filename):
    inputFile = open(filename, 'r')
    lines = inputFile.readlines()
    inputFile.close()
    return lines

def main():
    lines = readLinesFromFile('input.txt')
    # Parse the input data
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), lines)
    # Will be used to store count of clams occuping given X,Y fabric single square
    ground = defaultdict(int)
    for (claim_id, left_margin, top_margin, width, height) in claims:
        for x in range(width):
            for y in range(height):
                # put a +=1 count to a fabric single square at coordinates of single block
                # single block starts at left_margin and ends at left_margin + X width
                # single block start at top_margin and ends at top_margin + Y height
                ground[(left_margin + x, top_margin + y)] += 1
    # ground now contains every X,Y coordinate with a count of how many pieces of claims are on that particular X,Y point
    result = 0
    for (x,y), count in ground.items():
        # just count every X,Y where there are two or more claims for part I
        if count >= 2:
            result += 1
    print(result)
    
    # part 2 - now that the ground is built up, we can go through every claim and check if every X,Y of that claim has count == 1 meaning that this is claim not overlapping with other claims
    claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), lines)
    for (claim_id, left_margin, top_margin, width, height) in claims:
        cleanClaim = True
        for x in range(width):
            for y in range(height):
                if ground[(left_margin + x, top_margin + y)] > 1:
                    cleanClaim = False
        if cleanClaim:
            print(claim_id)

main()