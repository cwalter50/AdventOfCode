# Advent of Code 2024 Day 3
# https://adventofcode.com/2024/day/3

def readData():
    with open('2024/Day03-Python/sample.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        # print(lines)
        return lines

# search for Mul values in lines. looking for mul(4,10) exactly
def getMulValues(lines):
    for line in lines:
        loc = 0
        # closeLocation = 0
        count = 0
        while("mul(" in line[loc:]):

            print(f"location is {loc}. line is {line[loc:]}")

            loc = line[loc:].find("mul(")
            closeLocation = line[loc:].find(")")
            part = line[loc:closeLocation + 1]
            getSubstringValue(part)
            loc = closeLocation
            count += 1
            if count == 10:
                break
            


def getSubstringValue(part):
    print(part)
    



def part1(lines):
    

    getMulValues(lines)
    
    # print(f"Part1 answer is: {count}")

def part2(lines):
    rows = getLineNumbers(lines)

    count = 0
    for row in rows:
        if isSafe(row):
            count += 1
            # print(f"row {row} is safe")
        elif isIncreasingDampner(row) or isDecreasingDampner(row):
            count += 1
            # print(f"row {row} is safe")
    
    print(f"Part2 answer is: {count}")

lines = readData() 

part1(lines) 
# part2(lines)
