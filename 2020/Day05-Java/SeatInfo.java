
class SeatInfo {
  String original;
  int row;
  int column;
  int id; // = 8*row + column

  public SeatInfo(String o) {
    this.original = o;
    // first 7 are F or B
    // F and B act like binary numbers. F = 0, B = 1
    row = 0; // update this value, based on the f and b.
    for (int i = 0; i < 7; i++) {
      String current = o.substring(i, i + 1);
      if (current.equals("B")) {
        row += (int) Math.pow(2, 6 - i);
      }
    }
    // last 3 are R or L
    // R and L act like binary numbers. R = 1, L = 0
    this.column = 0; // update this value, based on the R and L.
    for (int i = 0; i < 3; i++) {
      String current = o.substring(i + 7, i + 8);
      if (current.equals("R")) {
        column += (int) Math.pow(2, 2 - i);
      }
    }

    this.id = 8 * row + column;
  }

  public String toString() {
    return "SeatInfo: " + this.original + ", row: " + this.row + ", column: " + this.column + ", id: " + this.id;

  }

  // compare seat rows first, then seat columns
  // return -1 if less, 0 if equal, 1 if greater
  public int compareTo(SeatInfo s)
  {
    if (this.id < s.id)
      return -1;
    else if (this.id == s.id)
      return 0;
    else
      return 1;
    // if (this.row == s.row && this.column == s.column)
    //   return 0;
    // else if (this.row < s.row)
    //   return -1;
    // else if (this.row > s.row)
    //   return 1;
    // else if (this.column < s.column)
    //   return -1;
    // else 
    //   return 1;
  }

}
