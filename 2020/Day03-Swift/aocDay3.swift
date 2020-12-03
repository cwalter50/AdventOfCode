import UIKit
import Foundation

/*
 About the challenge: Advent of Code Day 3
 https://adventofcode.com/2020/day/3
 */

var myStrings = [String]()
if let path = Bundle.main.path(forResource: "Day3Data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        myStrings = data.components(separatedBy: .newlines)
//        print(myStrings)
        // TextView.text = myStrings.joined(separator: ", ")
    } catch {
        print(error)
    }
}

// we now have each row in a [String] called myStrings

// last element in myStrings looks like ""... need to remove it.. bug in reading data...
myStrings.removeLast()

func findTreesForSlope(horizontalShift: Int, verticalShift: Int) -> Int
{
    var horizontalPos = 0 // keep track of horizontal shifts of 3
    var verticalPos = 0 // keep track of vertical shifts of 1

    var treeCount = 0 // keep track of trees

    while verticalPos < myStrings.count
    {
        var currentRow = myStrings[verticalPos]
        // we might have to add extra patterns to the right of the horizontal row. check the current rows length
        
        while horizontalPos >= currentRow.count
        {
            currentRow += currentRow
        }
        // check current location to see if it is a tree
        let currentChar = String(Array(currentRow)[horizontalPos])
//        print("verticalPos = \(verticalPos), horizontalPos = \(horizontalPos), character = \(currentChar)")
        if currentChar == "#"
        {
            treeCount += 1
        }
        
        // move right 3 down 1
        horizontalPos += horizontalShift
        verticalPos += verticalShift
        // check again by repeating this loop until we are at the last row
        
    }
    return treeCount
//    print(treeCount)

}

var oneOne = findTreesForSlope(horizontalShift: 1, verticalShift: 1)
var threeOne = findTreesForSlope(horizontalShift: 3, verticalShift: 1)
var fiveOne = findTreesForSlope(horizontalShift: 5, verticalShift: 1)
var sevenOne = findTreesForSlope(horizontalShift: 7, verticalShift: 1)
var oneTwo = findTreesForSlope(horizontalShift: 1, verticalShift: 2)

var part2Answer = oneOne*threeOne*fiveOne*sevenOne*oneTwo
print(part2Answer)
