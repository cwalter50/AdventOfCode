# Advent of Code 2021 Day 21
# https://adventofcode.com/2021/day/21


def readData():
    with open('data.txt') as f:
        lines = f.read().splitlines()
        
    #   nums = f.read().split(",")
    return lines

diceVal = 1
def simulate1Turn(start):
  # roll three times, add that sum to the start
  global diceVal
  total = 0
  for i in range(3):
    total += diceVal
    diceVal += 1
    if diceVal > 100:
      diceVal = 1

  start = (start + total)%10
  if start == 0:
    start = 10
  return start

def part1(p1Pos, p2Pos):
  p1Score = 0
  p2Score = 0
  isP1Turn = True
  diceRollCount = 0

  while (p1Score < 1000 and p2Score < 1000):
    if isP1Turn:
      result = simulate1Turn(p1Pos)
      p1Score += result
      p1Pos = result
      print("Adding " + str(result)+ " to p1: p1Score: "+ str(p1Score))
      diceRollCount += 3
      isP1Turn =  not isP1Turn
    else:
      result = simulate1Turn(p2Pos)
      p2Score += result
      p2Pos = result
      print("Adding " + str(result)+ " to p2: p2Score: "+ str(p2Score))
      diceRollCount += 3
      isP1Turn =  not isP1Turn

  # game over
  print("p1Score: "+ str(p1Score)+ " p2Score: "+ str(p2Score) + " diceRoll: "+ str(diceRollCount))
  if p1Score < p2Score:
    return p1Score * diceRollCount
  else:
    return p2Score * diceRollCount


def part2(p1Pos, p2Pos):
  p1Score = 0
  p2Score = 0
  isP1Turn = True
  diceRollCount = 0

  while (p1Score < 1000 and p2Score < 1000):
    if isP1Turn:
      result = simulate1Turn(p1Pos)
      p1Score += result
      p1Pos = result
      # print("Adding " + str(result)+ " to p1: p1Score: "+ str(p1Score))
      diceRollCount += 3
      isP1Turn =  not isP1Turn
    else:
      result = simulate1Turn(p2Pos)
      p2Score += result
      p2Pos = result
      # print("Adding " + str(result)+ " to p2: p2Score: "+ str(p2Score))
      diceRollCount += 3
      isP1Turn =  not isP1Turn

  # game over
  print("p1Score: "+ str(p1Score)+ " p2Score: "+ str(p2Score) + " diceRoll: "+ str(diceRollCount))
  if p1Score < p2Score:
    return p1Score * diceRollCount
  else:
    return p2Score * diceRollCount
    


theLines = readData()
player1Start = int(theLines[0].split(": ")[1])
player2Start = int(theLines[1].split(": ")[1])

print("Player 1 starts at " + str(player1Start))
print("Player 2 starts at " + str(player2Start))




    
part1Answer = part1(player1Start, player2Start)
print("Part 1 Answer: " + str(part1Answer))


part2Answer = part2(player1Start, player2Start)
print("Part 2 Answer: " + str(part2Answer))
