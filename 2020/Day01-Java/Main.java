/*
 * Question Details: https://adventofcode.com/2020/day/1 
 */

import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;

class Main {
  public static void main(String[] args) throws IOException {
    Scanner input = new Scanner(new File("data.txt"));

    ArrayList<Integer> list = new ArrayList<Integer>();

    while (input.hasNext()) {
      list.add(input.nextInt());
    }

    // System.out.println(list);

    for (int i = 0; i < list.size(); i++) {
      int current = list.get(i);
      for (int j = i + 1; j < list.size(); j++) {
        int next = list.get(j);
        if (current + next == 2020) {
          System.out.println(current + " + " + next + " = 2020 " + current + " * " + next + " = " + (current * next));
        }
      }
    }

    for (int i = 0; i < list.size(); i++) {
      int first = list.get(i);
      for (int j = i + 1; j < list.size(); j++) {
        int second = list.get(j);
        for (int k = j + 1; k < list.size(); k++) {
          int third = list.get(k);
          if (first + second + third == 2020) {
            System.out.println(first + " + " + second + " + " + third + " = 2020; " + first + " * " + second + " * "
                + third + " = " + (first * second * third));
          }
        }

      }
    }

  }
}

