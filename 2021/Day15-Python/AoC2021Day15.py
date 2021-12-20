# Advent of Code 2021 Day 15
# https://adventofcode.com/2021/day/15

# 1143 is the lowest that I found... It is still too high. My program was running for 20 minutes.

def readData():
    with open('2021/Day15-Python/data.txt') as f:
        lines = f.read().splitlines()
        
    #   nums = f.read().split(",")
    return lines

def printGrid(grid):
    result = ""
    for r in grid:
        for c in r:
            result += c
        result += "\n"
    print (result)

def copyPath(path):
    newPath = []
    for num in path:
        newPath.append(num)
    
    return newPath

paths = []
sums = []
minimum = 1300

def findNext(grid, path, x, y):
    global minimum
    height = len(grid) - 1
    width = len(grid[0]) - 1
    path2 = copyPath(path)
    path2.append(int(grid[y][x]))
    val = sum(path2)

    # stop searching if val is high
    if val < minimum:
        if y == height and x == width:
            # base case: at last position, bottom right
            # path.append(grid[height][width])
            paths.append(path2)
            total = sum(path2)
            # sums.append(total)
            if total < minimum:
                minimum = total
                print("Found new min " + str(minimum))
            # print(total)
        # move down or right
        # if x < width and int(grid[y][x+1]) != 9:
        if x < width:
            findNext(grid, path2, x+1, y)
        # if y < height and int(grid[y+1][x]) != 9:
        if y < height:
            findNext(grid, path2, x, y+1)




def part1(grid):

    # Brute Force: find all possible paths that move right and down from top left
    path = []
    # try to speed up process by throwing away paths that are too large.
    findNext(grid, path, 0, 0)

    # print(len(paths))
    # sums = []
    # for p in paths:
    #     sums.append(sum(p))
    global minimum
    return minimum - int(grid[0][0])
    
    # return min(sums) - int(grid[0][0])

def part2():
    
    return 0


theLines = readData()

grid = []

for line in theLines:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

# print(grid)
# printGrid(grid)

part1Answer = part1(grid)

print("Part 1 Answer: " + str(part1Answer))


part2Answer = part2()
print("Part2 Answer: " + str(part2Answer))
