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
            if (part.contains("red"))
                this.red = Integer.parseInt(part);
            else if (part.contains("green"))
                this.green = Integer.parseInt(part);
            else if (part.contains("blue"))
                this.red = Integer.parseInt(part);
        }

    }
}
