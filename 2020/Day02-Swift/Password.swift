import Foundation

class Password
{
  /* Sample:
  "2-5 w: dgqtwwkwwc" -> for the PW to be valid it needs 2-5 w's in the password. dgqtwwkwwc has 4 w's so it is valid

  try using this next time to break up a string into parts. My current solution is clunky 
  let fullName    = "First Last"
  let fullNameArr = fullName.components(separatedBy: " ")

  let name    = fullNameArr[0]
  let surname = fullNameArr[1]
  
  // This line has three different separators.
let line = "a:b,c;d"

// Create a CharacterSet of delimiters.
let separators = CharacterSet(charactersIn: ":,;")
// Split based on characters.
let parts = line.components(separatedBy: separators)
  
  */
  var original: String
  var pw: String // the password
  var min: Int // min times letter can appear
  var max: Int // max times letter can appear
  var letter: String // this is the letter in the Password

  init(o: String)
  {
    self.original = o;
    self.max = 0
    self.min = 0
    self.letter = "a"
    self.pw = "test"
    // serach for the dash -.
    let dashIndex = original.firstIndex(of: "-") ?? original.endIndex
    self.min = Int(original[..<dashIndex]) ?? 0
    let spaceIndex = original.firstIndex(of: " ") ?? original.endIndex
    let afterDashIndex = original.index(dashIndex, offsetBy: 1)
    self.max = Int(original[afterDashIndex..<spaceIndex]) ?? 0
    let afterSpaceIndex = original.index(spaceIndex, offsetBy:1)
    
    self.letter = String(original[afterSpaceIndex])
    let colonIndex = original.firstIndex(of: ":") ?? original.endIndex
    let afterColonIndex = original.index(after: colonIndex)
    self.pw = String(original[afterColonIndex..<original.endIndex])
    

    // print("\(original) min: \(min) max: \(max) letter: \(letter) password: \(pw)")

  }

  func isValid() -> Bool
  {
    var count = 0
    for character in self.pw
    {
      if String(character) == self.letter
      {
        count += 1
      }
    }

    if count >= self.min && count <= self.max
    {
      return true
    }
    else 
    {
      return false
    }
  }

  func isValid2() -> Bool
  {
    // dont have to worry about the -1 in the offset because pw has a space in front of it.
    let firstIndex = pw.index(pw.startIndex, offsetBy: min)
    let secondIndex = pw.index(pw.startIndex, offsetBy: max)

    // print(pw[firstIndex])
    // print(pw[secondIndex])
    let firstCorrect: Bool = String(pw[firstIndex]) == letter
    let secondCorrect: Bool = String(pw[secondIndex]) == letter
    
    var count = 0
    if firstCorrect {
        count += 1
    }
    if secondCorrect {
        count += 1
    }
    
    if count == 1
    {
        return true
    }
    else
    {
        return false
    }

  }

}
