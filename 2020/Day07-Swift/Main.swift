import UIKit
import Foundation

/*
 About the challenge: Advent of Code Day 7
 https://adventofcode.com/2020/day/7
 */

class Bag: CustomStringConvertible
{
    var color: String
    var contains: [String:Int]
    
    var description: String {
        var result = "\(color) contains "
        for item in contains
        {
            result += "\(item.value) \(item.key), "
        }
        return result
    }
    
    init(original: String)
    {
        let words = original.components(separatedBy: .whitespaces)
        color = words[0] + " " + words[1]
        contains = [String: Int]()
        var count = 5
        
        while count < words.count
        {
            let next = words[count] + " " + words[count+1]
            if next != "other bags." // other bags occurs if there are no other bags
            {
                contains[next] = Int(words[count-1]) ?? 1
            }
            
            count += 4
        }
    }
}



var myStrings = [String]()
if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        // Split based on characters.

        myStrings = data.components(separatedBy: .newlines)
    
    } catch {
        print(error)
    }
}
//print(myStrings)
myStrings.removeLast()

var myBags = [Bag]()

for word in myStrings
{
    myBags.append(Bag(original: word))
    
}

//print(myBags)


// myBags now contains all of the info needed for this problem


/*
 Algorithm for part 1
 1.if bag . contains shiny gold add it to the list of valid bags
 ,
 
 2. search my bags for any bags that are in valid bags
 3. repeat step 2 until the search returns 0 results
 
 */

var validBags = [Bag]()


func addToValidBags(bag: Bag) -> Bool
{
    // add it to the list of valid bags if its not in it already
    if !validBags.contains(where: {$0.color == bag.color})
    {
        validBags.append(bag)
        print(bag)
        return true
    }
    else {
        return false
    }
}

// 1
for bag in myBags
{
    if bag.contains.keys.contains("shiny gold")
    {
        addToValidBags(bag: bag)
    }
}

//2
var foundAtLeast1NewBag = true
while(foundAtLeast1NewBag == true)
{
    foundAtLeast1NewBag = false
    for bag in validBags
    {
        for comparedBag in myBags
        {
            if comparedBag.contains.keys.contains(bag.color)
            {
                if addToValidBags(bag: comparedBag) == true
                {
                    foundAtLeast1NewBag = true
                }
                
            }
        }
    }
}

print(validBags.count)

/*
 Algorithm for part 2
 1. count the number of bags in a shiny gold bag
 2. for each bag in shiny gold bag, count those number of bags
 3. for each bag in those gold bags, count those number of bags
 
 
 */

func numberOfBags(bag: Bag) -> Int
{
    // base case
    if bag.contains.count == 0
    {
        return 0
    }
    // otherwise count them up
    var count = 0
    for item in bag.contains
    {
        if let newBag = myBags.first(where: {$0.color == item.key})
        {
            count += item.value + item.value * numberOfBags(bag: newBag) // recursive call
        }
        else {
            print("couldn't find bag \(item.key)")
        }
    }
    
    return count
}

if let shinyGoldBag = myBags.first(where: {$0.color == "shiny gold"}) {
    let total = numberOfBags(bag: shinyGoldBag)

    print(total)
}
else {
    print("NO SHINY GOLD BAG!!!!")
}







