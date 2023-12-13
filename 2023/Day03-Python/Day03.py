# Advent of Code 2023 Day 3
# https://adventofcode.com/2023/day/3

def readData():
    with open('2023/Day03-Python/data.txt') as f:
        # lines = f.readlines()
        lines = f.read().splitlines()
        # print(lines)
        return lines
    
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
class Card:
  def __init__(self, line):
    parts = line.split(":")
    self.cardNum = (parts[0].split(" "))[-1]
    nums = parts[1].split("|")
    # print(nums[0] + "END")
    # print(nums[1] + "END")
    part0 = nums[0].replace('  ', ' ')
    part0 = part0.strip()
    self.winNums = []
    for part in part0.split(' '):
        self.winNums.append(part.strip())
    
    part1 = nums[1].replace('  ', ' ')
    part1 = part1.strip()
    self.myNums = []
    for part in part1.split(' '):
        self.myNums.append(part.strip())
    
    # self.winNums = [str(s.strip()) for s in nums[0].strip().split(" ")]
    # self.myNums = [str(s.strip()) for s in nums[1].strip().split(" ")]


def getCards(lines):
    cards = []

    for line in lines:
        card = Card(line)
        cards.append(card)
    
    return cards



def part1(lines):
    cards = getCards(lines)

    total = 0
    for card in cards:
        matchingVals = []
        matches = 0
        for num in card.winNums:
            if num in card.myNums:
                matches += 1
                matchingVals.append(num)
        winning = 0
        if matches > 0:
            winning = 2 ** (matches-1)
        total += winning

        # print("Card " + card.cardNum + " win:" + str(winning))
        # print(*matchingVals)
    part1Answer = total
    print("Part1 answer is: " + str(part1Answer))

def part2(lines):
    nums = []
    # for line in lines:
    #     lineNums = getLineNumbers2(line)
    #     first = lineNums[0]
    #     last = lineNums[-1]
    #     # adjust the lineNums if there are wordNums in the list
        
    #     num = first * 10 + last
    #     nums.append(num)
    # # print(nums)
    # part2Answer = sum(nums)
    # print("Part2 answer is: " + str(part2Answer))

   
lines = readData() 
# cards = getCards(lines)

part1(lines) 
# part2(lines)
