# Advent of Code 2024 Day 1
# https://adventofcode.com/2024/day/1

def readData():
    with open('2024/Day01-Python/data.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        # print(lines)
        return lines

# this will convert each line into an array of numbers on the left and an array of numbers on the right
def getLeftAndRightNumbers(lines):
    left = []
    right = []
    for line in lines:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    
    # print(left)
    # print(right)
    return [left, right]

def part1(lines):
    result = getLeftAndRightNumbers(lines)
    # print(result)
    leftNums = result[0]
    rightNums = result[1]
    leftNums.sort()
    rightNums.sort()
    
    total = 0
    for i in range(len(leftNums)):
        total += abs(rightNums[i] - leftNums[i])
        # print(f"adding {rightNums[i] - leftNums[i]} to total")
    
    # print(total)
    print("Part1 answer is: " + str(total))

def part2(lines):
    result = getLeftAndRightNumbers(lines)
    # print(result)
    leftNums = result[0]
    rightNums = result[1]
    leftNums.sort()
    rightNums.sort()
    total = 0
    for i in range(len(leftNums)):
        left = leftNums[i]
        count = rightNums.count(left)
        total += left * count

    # print(nums)
    print("Part2 answer is: " + str(total))

   
lines = readData() 

part1(lines) 
part2(lines)
