# Advent of Code 2021 Day 13
# https://adventofcode.com/2021/day/13

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Direction:
  def __init__(self,axis,val):
    self.axis = axis
    self.val = val


def readData():
    with open('data.txt') as f:
        lines = f.read().splitlines()

        
    #   nums = f.read().split(",")
      
        # lines = f.read().splitlines()
      
    return lines

def printGrid(grid):
  result = ""
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      result += grid[r][c] + " "
    result += "\n"
  print(result)


def part1(coordinates, directions):
  grid =[]
  for r in range(1500):
    grid.append([])
    for c in range(1500):
      grid[r].append(".")

  # get first direction
  d = directions[0]

  for p in coordinates:
    if d.axis == "y":
      if p.y > d.val:
        p.y = d.val - (p.y - d.val)
    else:
      if p.x > d.val:
        p.x = d.val - (p.x - d.val)
    

  for p in coordinates:
    grid[p.y][p.x] = "#"

  # printGrid(grid)
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == "#":
        count += 1

  return count

def part2(coordinates, directions):
  grid =[]
  for r in range(10):
    grid.append([])
    for c in range(40):
      grid[r].append(".")

  for d in directions:
    for p in coordinates:
      if d.axis == "y":
        if p.y > d.val:
          p.y = d.val - (p.y - d.val)
      else:
        if p.x > d.val:
          p.x = d.val - (p.x - d.val)
      
  for p in coordinates:
    grid[p.y][p.x] = "#"

  printGrid(grid)
  return 0


theLines = readData()

points = []
directions = []

for i in range(0,982):
  coor = theLines[i].split(",")
  p = Point(int(coor[0]), int(coor[1]))
  points.append(p)
  print(str(p.x)+","+str(p.y))

for i in range(983,995):
  dir = theLines[i].split("=")
  d = Direction(dir[0][-1], int(dir[1]))
  print(d.axis + ": " + str(d.val))
  directions.append(d)


part1Answer = part1(points, directions)
print("Part 1 Answer: " + str(part1Answer))

# reset Nums
# nums = readData()
part2Answer = part2(points, directions)
print("Part2 Answer: Look at the terminal Output! " + str(part2Answer))
