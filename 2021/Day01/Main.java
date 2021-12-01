// https://adventofcode.com/2021/day/1

import java.util.Scanner;
import java.io.File;
import java.io.IOException;

class Main 
{
  public static void main(String[] args) throws IOException
  {

    Scanner scan = new Scanner(new File("data.txt"));

    int [] list = new int[2000];

    for(int i = 0; i < 2000; i++)
    {
      int num = scan.nextInt();
      list[i] = num;
      // System.out.println(num);
    }
    // Part 1
    int answer = part1(list);
    System.out.println(answer);

    // Part 2:
    int answer2 = part2(list);
    System.out.println(answer2);

  }

  public static int part1(int[] list)
  {
    int count = 0;
    for (int i = 0; i < list.length-1;i++)
    {
      int num = list[i];
      int num2 = list[i+1];
      if (num < num2)
        count++;
    }
    return count;
  }

    public static int part2(int[] list)
  {
    int count = 0;
    for (int i = 0; i < list.length-3;i++)
    {
      int num = list[i]+list[i+1]+list[i+2];
      int num2 = list[i+1]+list[i+2]+list[i+3];
      if (num < num2)
        count++;
    }
    return count;
  }
}
