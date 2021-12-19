# Advent of Code 2021 Day 14
# https://adventofcode.com/2021/day/14

class Direction:
  def __init__(self, a, b, insert):
    self.a = a
    self.b = b
    self.insert = insert

def readData():
    with open('2021/Day14-Python/sample.txt') as f:
        lines = f.read().splitlines()
        
    #   nums = f.read().split(",")
    return lines



def part1(directions):
    # loop through the template getting 2 letters at a time and 
    # matching it with a direction, then insert
    result = template

    for step in range(10):

        for i in range(0,2*len(result)-2,2):
            first = result[i]
            second = result[i+1]
            valList = [x for x in directions if x.a == first and x.b == second]
            # there should only be 1 thing in valList which is the only direction
            dir = valList[0]
            # print(dir.a + dir.b + " -> "+ dir.insert)

            result = result[:i+1] + dir.insert + result[i+1:]

    # count how often each character appears in result
    max = 0
    min = 10000000000000000
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alphabet)):
        num = result.count(alphabet[i])
        if num > 0 and num < min:
            min = num
        if num > 0 and num > max:
            max = num

    return max-min

def part2(directions):
    # loop through the template getting 2 letters at a time and 
    # matching it with a direction, then insert
    result = template
    dict = {}

    # add original result into dictionary
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        dict[letter] = 0
    for i in range(len(result)):
        dict[result[i]] += 1

    for step in range(40):

        for i in range(0,2*len(result)-2,2):
            first = result[i]
            second = result[i+1]
            valList = [x for x in directions if x.a == first and x.b == second]
            # there should only be 1 thing in valList which is the only direction
            dir = valList[0]
            # print(dir.a + dir.b + " -> "+ dir.insert)

            result = result[:i+1] + dir.insert + result[i+1:]
            dict[dir.insert] += 1
            # print(result)
        # print(result)
        print("Finished step "+ str(step))

    # remove all zeros from dictionary
    finalDict = {key:val for key, val in dict.items() if val != 0}
    vals = finalDict.values()
    theMax = max(vals)
    theMin = min(vals)

    return theMax-theMin


theLines = readData()

template = theLines[0]

print(template)

directions = []

for i in range(2, len(theLines)):
    parts = theLines[i].split(" -> ")
    # print(parts)
    d = Direction(parts[0][0], parts[0][1], parts[1])
    directions.append(d)

part1Answer = part1(directions)
print("Part 1 Answer: " + str(part1Answer))


part2Answer = part2(directions)
print("Part2 Answer: " + str(part2Answer))
