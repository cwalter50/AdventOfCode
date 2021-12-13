# Advent of Code 2021 Day 11
# https://adventofcode.com/2021/day/11

def readData():
    with open('2021/Day11-Python/data.txt') as f:
        # lines = f.read().splitlines()
        lines = f.read().splitlines()
    #   nums = f.read().split(",")
        # print(lines)
        # lines = f.read().splitlines()
    return lines

def getGrid(lines):
    grid = []

    for line in lines:
        list = []
        for number in line:
            list.append(int(number))
        grid.append(list)
    
    # grid should be 10 by 10 now...
    return grid

def flashOctopus(flashGrid, grid, row, col):
    # only flash if value is greater than 9
    if grid[row][col] > 9 and flashGrid[row][col] == False:
        # grid[row][col] += 1
        flashGrid[row][col] = True
        # check the 8 surrounding locations
        if row >= 1:
            grid[row-1][col] += 1
            flashOctopus(flashGrid, grid, row-1,col)
        if row >= 1 and col >=1:
            grid[row-1][col-1] += 1
            flashOctopus(flashGrid, grid, row-1,col-1)
        if row >= 1 and col < 9:
            grid[row-1][col+1] += 1
            flashOctopus(flashGrid, grid, row-1,col+1)
        if col >= 1:
            grid[row][col-1] += 1
            flashOctopus(flashGrid, grid, row,col-1)
        if col < 9:
            grid[row][col+1] += 1
            flashOctopus(flashGrid, grid, row,col+1)
        if row < 9:
            grid[row+1][col] += 1
            flashOctopus(flashGrid, grid, row+1,col)
        if row < 9 and col >= 1:
            grid[row+1][col-1] += 1
            flashOctopus(flashGrid, grid, row+1,col-1)
        if row < 9 and col < 9:
            grid[row+1][col+1] += 1
            flashOctopus(flashGrid, grid, row+1,col+1)
        

# this will return the number of flashes that happened in the day
def simulate1Day(grid):
    # make a hasFlashedGrid that will be a bunch of False. If it flashes, turn it to true
    flashGrid = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append(False)
        flashGrid.append(row)

    # step 1: add 1 to every octopus
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1

    # step 2: flash every octopus > 9. That will also flash all adjacent octopus 
    for i in range(10):
        for j in range(10):
            if flashGrid[i][j] == False:
                flashOctopus(flashGrid, grid, i, j)

    # step 3: Count how many octopus have a value >= 9. Those all flashed. reset them to 0
    
    # print(grid)
    count = 0
    for r in range(10):
        for c in range(10):
            if grid[r][c] > 9:
                count += 1
                grid[r][c] = 0
    # print(grid)
            
    return count

def printGrid(grid):
    result = ""
    for r in range(10):
        for c in range(10):
            result += str(grid[r][c])
        result += "\n"
    print(result)

def part1(grid):
    # printGrid(grid)
    total = 0
    for i in range(0,100):
        total += simulate1Day(grid)
    # total = simulate1Day(grid)
    # total += simulate1Day(grid)
    printGrid(grid)
    return total

def allFlashed(grid):
    for r in range(0,10):
        for c in range(0,10):
            if grid[r][c] != 0:
                return False
    return True


def part2(grid):
    count = 0
    while (allFlashed(grid) == False):
        simulate1Day(grid)
        count += 1
    
    return count


theLines = readData()  

theGrid = getGrid(theLines)
# print(theGrid)
# print(nums)

part1Answer = part1(theGrid)
print("Part 1 Answer: " + str(part1Answer))

# reset Nums
theLines = readData()
theGrid = getGrid(theLines)
part2Answer = part2(theGrid)
print("Part2 Answer: " + str(part2Answer))
