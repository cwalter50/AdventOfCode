/*
Here are the details about the challenge:
https://adventofcode.com/2020/day/2
*/

import Foundation


if let path = Bundle.main.path(forResource: "data", ofType: "txt") {
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        let myStrings: [String] = data.components(separatedBy: .newlines) 
        // print(myStrings)

        var count = 0
        var count2 = 0
        for entry in myStrings
        {
          // find the dash and colon
          let current = Password(o: entry)
          if (current.isValid())
          {
            count += 1
          }
          if (current.isValid2())
          {
            count2 += 1
          }
          // print(current.isValid())
        }
        print(count)
        print(count2)
        
    } catch {
        print(error)
    }
}

