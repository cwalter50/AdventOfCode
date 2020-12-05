import java.util.Scanner;
import java.util.ArrayList;
import java.io.IOException;
import java.io.File;

/*
 About the challenge: Advent of Code Day 5
 https://adventofcode.com/2020/day/5
 
 Small Sample Data
 BFFFBBFRRR: row 70, column 7, seat ID 567.
 FFFBBBFRRR: row 14, column 7, seat ID 119.
 BBFFBBFRLL: row 102, column 4, seat ID 820.
 */

class Main {
  public static void main(String[] args) throws IOException {
    Scanner input = new Scanner(new File("data.txt"));

    ArrayList<String> list = new ArrayList<String>();

    while (input.hasNext()) {
      list.add(input.nextLine());
    }

    // System.out.println(list);
    ArrayList <SeatInfo> seats = new ArrayList <SeatInfo>();

    int max = 0; // find max
    for (String item : list) {
      SeatInfo current = new SeatInfo(item);
      seats.add(current);
      // System.out.println(current);
      if (current.id > max)
        max = current.id;
    }
    System.out.println(max);

    // sort the seats...
    for (int i = 0; i < seats.size()-1; i++)
    {
      for (int j = 0; j < seats.size()-i-1; j++)
      {
        SeatInfo first = seats.get(j);
        SeatInfo second = seats.get(j+1);
        if (first.compareTo(second) > 0)
        {
          // swap first and second
          SeatInfo temp = first;
          seats.set(j,second);
          seats.set(j+1,temp);
        }
      }
    }

    // seats are now sorted... find the missing number
    int start = seats.get(0).id;

    for (int i = 0; i < seats.size(); i++)
    {
      int current = seats.get(i).id;
      if (current != start)
      {
        System.out.println(current);
        break;
      }
        
      start++;
    }

    // System.out.println(seats.size());
    for (SeatInfo s: seats)
    {
      System.out.println(s.id);
    }
    // System.out.println(seats);


  }
}
