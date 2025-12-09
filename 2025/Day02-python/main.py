# Advent of Code 2025 Day 2
# https://adventofcode.com/2025/day/2

def readData():
    with open('2025/Day02-python/data.txt') as f:
        # lines = f.readlines()
        lines = f.read().split(",")
        # print(lines)
        return lines
    
def isValidID(num):
    middle = len(num) // 2
    left = num[:middle]
    right = num[middle:]
    # print(f"left: {left}, right: {right}")
    if left == right:
        return True
    return False

def isValidIDPart2(num):
    for i in range(1, len(num) // 2 + 1):
        substring = num[:i]
        # determine how many times you need to repeat substring to reach length of num
        repeat_count = len(num) // len(substring)
        possible = substring * repeat_count
        if possible == num:
            return True
        
    return False
        




def findInvalidIDs(num1, num2):
    a = int(num1)
    b = int(num2)
    valid_ids = []
    for i in range(a, b + 1):
        if isValidID(str(i)):
            valid_ids.append(i)
            # print(i)
    return valid_ids

def findInvalidIDsPart2(num1, num2):
    a = int(num1)
    b = int(num2)
    valid_ids = []
    for i in range(a, b + 1):
        if isValidIDPart2(str(i)):
            valid_ids.append(i)
            # print(i)
    return valid_ids


def part1(lines):

    valid_ids = []
    for line in lines:
        parts = line.split("-")
        # print(parts)
        newIds = findInvalidIDs(parts[0], parts[1])
        # print(newIds)
        valid_ids += newIds

    total = 0
    for val in valid_ids:
        # print(val)
        total += val
    


    print("Part1 answer is: " + str(total))

def part2(lines):
    valid_ids = []
    for line in lines:
        parts = line.split("-")
        # print(parts)
        newIds = findInvalidIDsPart2(parts[0], parts[1])
        # print(newIds)
        valid_ids += newIds

    total = 0
    for val in valid_ids:
        # print(val)
        total += val
    


    print("Part2 answer is: " + str(total))

   
lines = readData() 

part1(lines) 
part2(lines)
