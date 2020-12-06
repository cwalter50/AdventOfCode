import UIKit
import Foundation

/*
 About the challenge: Advent of Code Day 6
 https://adventofcode.com/2020/day/6
 */

var myStrings = [String]()
if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        // Split based on characters.
//        let parts = line.components(separatedBy: separators)
        myStrings = data.components(separatedBy: "\n\n")
    
    } catch {
        print(error)
    }
}
//print(myStrings)

// remove all \n from the string
var newStrings = [String]()
for group in myStrings
{
    var result = group.replacingOccurrences(of: "\n", with: "", options: NSString.CompareOptions.literal, range: nil)
    newStrings.append(result)
}
//print(newStrings)

// newStrings now contains everything that we need without the \n
var total = 0
let alphabet = "abcdefghijklmnopqrstuvwxyz"
for group in newStrings
{
    var count = 0
    for char in alphabet
    {
        if group.contains(char)
        {
            count += 1
        }
    }
//    print(count)
    total += count
}


print(total)


// PART 2
var myGroups = [String]()
if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        // Split based on characters.
        myGroups = data.components(separatedBy: .newlines)
    
    } catch {
        print(error)
    }
}
//print(myGroups)

// myGroups is now separated by lines.. Each group ends at a space


var newGroups = [[String]]()
var newGroup = [String]() // this will be reused over and over again
for subgroup in myGroups
{
   if subgroup != ""
   {
    newGroup.append(subgroup)
   }
   else
   {
    // end the new group...after adding it to newGroups
    newGroups.append(newGroup)
    newGroup.removeAll()
   }
    
}

// newGroups now has everything we need
//print(newGroups)

var totalCount = 0

for group in newGroups
{
    var count = 0
    for char in group[0]
    {
        var isFoundInEveryItem = true
        for sub in group
        {
            if !sub.contains(char)
            {
                isFoundInEveryItem = false
            }
        }
        if isFoundInEveryItem
        {
            count += 1
        }
    }
    totalCount += count
//    print(count)
}

print(totalCount)
