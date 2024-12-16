# Advent of Code 2024 Day 2
# https://adventofcode.com/2024/day/2

def readData():
    with open('2024/Day02-Python/data.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        # print(lines)
        return lines

# this will convert each line into an array of numbers 
def getLineNumbers(lines):
    rows = []
    for line in lines:
        numbers = [int(x) for x in line.split()]
        rows.append(numbers)
    # print(rows)
    return rows

def isIncreasing(row):
    safe = True
    for i in range(len(row)-1):
        curr = row[i]
        next = row[i+1]
        if curr >= next or next - curr > 3:
            safe = False
    return safe

def isDecreasing(row):
    safe = True
    for i in range(len(row)-1):
        curr = row[i]
        next = row[i+1]
        if curr <= next or curr - next > 3:
            safe = False
    return safe

def isSafe(row):
    return isIncreasing(row) or isDecreasing(row)   

def isIncreasingDampner(row):
    # apply dampner and we can remove one num that makes the row unsafe. 
    # Make two copies of row. One where we remove at i and check and another where we remove at i+1 and check
    rowCopy = []
    rowCopyNext = []
    for num in row:
        rowCopy.append(num)
        rowCopyNext.append(num)
    # print(f"row before removing dampner increasing {rowCopy}")
    if isIncreasing(row):
        return True
    for i in range(len(rowCopy)-1):
        curr = rowCopy[i]
        next = rowCopy[i+1]
        if curr >= next or next - curr > 3:
            del rowCopy[i]
            del rowCopyNext[i+1]
            break
    # print(f"row after removing dampner increasing {rowCopy}")
        
    return isSafe(rowCopy) or isSafe(rowCopyNext)

def isDecreasingDampner(row):

    # apply dampner and we can remove one num that makes the row unsafe
    # Make two copies of row. One where we remove at i and check and another where we remove at i+1 and check
    rowCopy = []
    rowCopyNext = []
    for num in row:
        rowCopy.append(num)
        rowCopyNext.append(num)
    # print(f"row before removing dampner decreasing {rowCopy}")
    if isDecreasing(row):
        return True
    for i in range(len(row)-1):
        curr = rowCopy[i]
        next = rowCopy[i+1]
        if curr <= next or curr - next > 3:
            del rowCopy[i]
            del rowCopyNext[i+1]
            break
    # print(f"row after removing dampner decreasing {rowCopy}")
    return isSafe(rowCopy) or isSafe(rowCopyNext)


def part1(lines):
    rows = getLineNumbers(lines)

    count = 0
    for row in rows:
        if isIncreasing(row) or isDecreasing(row):
            count += 1
            # print(f"row {row} is safe")
    
    print(f"Part1 answer is: {count}")

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
part2(lines)
