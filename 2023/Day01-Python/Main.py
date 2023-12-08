# Advent of Code 2024 Day 1
# https://adventofcode.com/2024/day/1

def readData():
    with open('2023/Day01-Python/data.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        # print(lines)
        return lines

# this will find the first and last number in a line, and put those numbers together
def getLineNumbers(line): 
    nums = []
    for symbol in line:
        if symbol.isdigit():
            nums.append(int(symbol))
    # print(nums)

    return nums

# this is a helper method to help with part 2, where some numbers are 2 or two
# will return number if it is or -1 if it is not a number
def isNumber(substring):
    wordNums = {
        'one': 1, 
        'two': 2, 
        'three': 3, 
        'four': 4, 
        'five': 5, 
        'six': 6, 
        'seven': 7, 
        'eight': 8, 
        'nine': 9, 
        'zero': 0, 
        '1':1, 
        '2':2, 
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '0':0
        }
    for item in wordNums.items():
        s2 = substring[0:len(item[0])]
        if s2 == item[0]:
            return item[1]
    
    return -1
def getLineNumbers2(line):
    nums = []
    for i in range(0, len(line)):
        substring = line[i:len(line)]
        num = isNumber(substring) # this returns the num or -1
        if num > -1:
            nums.append(num)
    # print(nums)

    return nums

    

def findWordNums(line):
    wordNums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
    lineNums = getLineNumbers(line)
    first = lineNums[0]
    last = lineNums[-1]
    firstPos = line.find(str(first))
    beginning = line[0:firstPos]
    lowest = -1
    lowestWord = ""
    for word in wordNums:
        possibleLow = beginning.find(word)
        # if possibleLow >= 0 and possibleLow  beginning:

def part1(lines):
    nums = []
    for line in lines:
        lineNums = getLineNumbers(line)
        first = lineNums[0]
        last = lineNums[-1]
        num = first * 10 + last
        nums.append(num)
    # print(nums)
    part1Answer = sum(nums)
    print("Part1 answer is: " + str(part1Answer))

def part2(lines):
    nums = []
    for line in lines:
        lineNums = getLineNumbers2(line)
        first = lineNums[0]
        last = lineNums[-1]
        # adjust the lineNums if there are wordNums in the list
        
        num = first * 10 + last
        nums.append(num)
    # print(nums)
    part2Answer = sum(nums)
    print("Part2 answer is: " + str(part2Answer))

   
lines = readData() 

part1(lines) 
part2(lines)
