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
    self.numMatches = 0 # this is for part2 and will be adjusted later
    self.numCards = 1 # this is for part2
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
    cards = getCards(lines)

    for i in range(len(cards)):
        for num in cards[i].winNums:
            if num in cards[i].myNums:
                cards[i].numMatches += 1
    # matches are now accurate for each card
                
    for i in range(len(cards)):
        for j in range(cards[i].numMatches):
            if i+j+1 < len(cards):
                cards[i+j+1].numCards += 1*cards[i].numCards
    # numCards are now accurate for each card
    
    total = 0
    for card in cards:
        total += card.numCards
    part2Answer = total
    print("Part2 answer is: " + str(part2Answer))

   
lines = readData() 
# cards = getCards(lines)

part1(lines) 
part2(lines)
