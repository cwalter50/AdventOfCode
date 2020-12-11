
/*
 * Question Details: 
 Day 9
 https://adventofcode.com/2020/day/9 
 */

import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;

class Main {
  public static void main(String[] args) throws IOException {
    Scanner input = new Scanner(new File("data.txt"));

    ArrayList<Long> list = new ArrayList<Long>();

    while (input.hasNext()) {
      list.add(input.nextLong());
    }

    // System.out.println(list);

    int preamble = 5;

    int count = preamble;
    boolean foundMatch = true;
    long next = list.get(preamble);

    while (count < list.size() && foundMatch == true) {
      next = list.get(count); // try to match next using the preamble numbers before it...
      foundMatch = false;
      for (int i = count - preamble; i < count - 1; i++) {
        long current = list.get(i);
        for (int j = i + 1; j < count; j++) {
          long second = list.get(j);
          if (current + second == next)
            foundMatch = true;
        }
      }

      if (foundMatch == false)
        System.out.println("couldn't find match for " + next + " at position " + count);
      count++;

    }

    // long part2Sum = 127;
    long part2Sum = 393911906;

    // sum up 2 consecutive nums, then 3, then 4, then 5, etc... until you find
    // match

    boolean foundSum = false;
    int totalNums = 2;
    long[] arr = new long[5];

    while (foundSum == false || totalNums > 20) {
      for (int i = 0; i < list.size() - totalNums + 1; i++) {
        int counter = 0;
        long sum = 0;
        while (counter < totalNums) {
          sum += list.get(i + counter);
          counter++;
        }
        if (sum == part2Sum) {
          String result = "Found Winner!!!: ";
          int count2 = 0;
          arr = new long[totalNums];
          while (count2 < totalNums) {
            result += list.get(i + count2) + " + ";

            arr[count2] = list.get(i + count2);
            count2++;
          }
          result += " = " + part2Sum;
          System.out.println(result);
          // mind min and max of arr

          long max = arr[0];
          long min = arr[0];

          for (int k = 0; k < arr.length; k++) {
            if (arr[k] > max)
              max = arr[k];
            if (arr[k] < min)
              min = arr[k];
          }

          System.out.println("Max: " + max + ", Min: " + min + " = " + (max + min));
          break;
        }
      }
      totalNums++; // try all over again with finding 3 contiguos nums, then 4, then 5, etc..
    }

  }

}
