import java.util.*;
import java.io.*;

public class Set {
    int red;
    int blue;
    int green;

    public Set(int red, int blue, int green) {
        this.red = red;
        this.blue = blue;
        this.green = green;
    }

    // this will be a string like 8 green, 6 blue, 20 red  or just 20 green
    public Set(String setString) {
        this.red = 0;
        this.green = 0;
        this.blue = 0;
        String[] parts = setString.split(",");
        for( String part: parts) {
            part = part.trim();
            String[] nums = part.split(" ");
            if (part.contains("red")) 
                if (nums[0] != null)
                    this.red = Integer.parseInt(nums[0]);
            if (part.contains("green"))
                if (nums[0] != null)
                    this.green = Integer.parseInt(nums[0]);
            if (part.contains("blue"))
                if (nums[0] != null)
                    this.blue = Integer.parseInt(nums[0]);
        }
        // System.out.println("Found " + red + " red, "+ green + " green, " + blue + " blue");

    }
}
