import java.util.*;
import java.io.*;
class Main 
{

  public static ArrayList <ArrayList<Node>> allPaths = new ArrayList<ArrayList<Node>>();

  public static ArrayList <ArrayList<Node>> allPaths2 = new ArrayList<ArrayList<Node>>();

  public static void main(String[] args) throws IOException
  {
    ArrayList<Node> nodes = getNodes();

    int part1Answer = part1(nodes);
    System.out.println("Part1Answer: "+part1Answer);

    int part2Answer = part2(nodes);
    System.out.println("Part2Answer: "+part2Answer);
    
  }

  public static int part2(ArrayList<Node> nodes)
  {
    Node start = nodes.get(findStart(nodes));
    // start a new path and find all paths
    ArrayList<Node> path = new ArrayList<Node>();
    path.add(start);
    hasNextNodePart2(start, path); // recursive method... that will make copies of a path and keep adding successful paths to allPaths.
      
    return allPaths2.size();
    // return 0;
  }

  public static boolean hasDuplicateSmall(ArrayList<Node> path)
  {
    for (int i = 0; i < path.size(); i++)
    {
      String outer = path.get(i).getValue();
      for (int j = i+1; j < path.size(); j++)
      {
        String inner = path.get(j).getValue();
        if (!outer.toUpperCase().equals(outer) && outer.equals(inner))
          return true;
      }
    }
    return false;
  }

  public static void hasNextNodePart2(Node current, ArrayList<Node> path)
  {
    for (Node n: current.getConnections())
    {
      if (n.isBig() == false && pathContains(path,n)) {
        // check for a duplicate small already
        if (!n.getValue().equals("start") && !n.getValue().equals("end") && !hasDuplicateSmall(path))
        {
          ArrayList<Node> path2 = copyPath(path);
          path2.add(n);
          hasNextNodePart2(n, path2);
        }

      }
      else if (n.getValue().equals("end"))
      {
        // copy path.... add n, then return true
        ArrayList<Node> path2 = copyPath(path);
        path2.add(n);
        allPaths2.add(path2);
        // System.out.println("Added Path: "+ path2);
      }
      else 
      {
        ArrayList<Node> path2 = copyPath(path);
        path2.add(n);
        hasNextNodePart2(n, path2);
      }
    }
  }

  public static ArrayList<Node> copyPath(ArrayList<Node> path)
  {
    ArrayList<Node> path2 = new ArrayList<Node>();
    for (Node n: path)
    {
      path2.add(n);
      // System.out.print(n + ": connections in copyPath: ");
      // System.out.println(n.getConnections());
    }
      
    return path2;
        
  }

  public static boolean pathContains(ArrayList<Node> path, Node node)
  {
    for (Node n : path)
    {
      if (n.getValue().equals(node.getValue()))
        return true;
    }

    return false;
  }


  public static void hasNextNode(Node current, ArrayList<Node> path)
  {
    for (Node n: current.getConnections())
    {
      if (n.isBig() == false && pathContains(path,n)) {
      }
      else if (n.getValue().equals("end"))
      {
        // copy path.... add n, then return true
        ArrayList<Node> path2 = copyPath(path);
        path2.add(n);
        allPaths.add(path2);
        // System.out.println("Added Path: "+ path2);
      }
      else 
      {
        ArrayList<Node> path2 = copyPath(path);
        path2.add(n);
        hasNextNode(n, path2);
      }
    }
  }
  

  public static int part1(ArrayList<Node> nodes)
  {
    // find start Node. then find all permutations that get you to the end.
    // System.out.println(nodes);
    Node start = nodes.get(findStart(nodes));
    // start a new path and find all paths
    ArrayList<Node> path = new ArrayList<Node>();
    path.add(start);
    hasNextNode(start, path); // recursive method... that will make copies of a path and keep adding successful paths to allPaths.
      
    return allPaths.size();
  }

  public static int findStart(ArrayList<Node> nodes)
  {
    for (int i = 0; i < nodes.size(); i++)
    { 
      Node node = nodes.get(i);
      if (node.getValue().equals("start"))
        return i;
    }
    return -1;
  }

  public static Node findNode(ArrayList<Node> nodes, String val)
  {
    for (Node n: nodes)
    {
      if (n.getValue().equals(val))
        return n;
    }
    return new Node("none");
  }


  public static ArrayList<Node> getNodes() throws IOException
  {
    ArrayList<Node> nodes = new ArrayList<Node>();

    Scanner scan = new Scanner(new File("data.txt"));

    while(scan.hasNext())
    {
      String[] parts = scan.nextLine().split("-");
      Node a = new Node(parts[0]);
      Node b = new Node(parts[1]);
      
      // int location = nodes.indexOf(a);
      int location = -1;
      for (int i = 0; i < nodes.size(); i++)
        if (nodes.get(i).equals(a))
          location = i;
      // System.out.println("indexOf "+ a + ": "+ location);

      if (location >= 0)
        nodes.get(location).addConnection(b);
      else 
      {
        a.addConnection(b);
        nodes.add(a);
      }
      location = -1;
      for (int i = 0; i < nodes.size(); i++)
        if (nodes.get(i).equals(b))
          location = i;
      if (location >= 0)
        nodes.get(location).addConnection(a);
      else 
      {
        b.addConnection(a);
        nodes.add(b);
      }
    }

    // nodes are correct and so are there connections. The connections of the connections are NOT correct... Fix them by matching them with the correct nodes

    for (Node n: nodes)
    {
      for (Node c: n.getConnections())
      {
        Node correct = findNode(nodes, c.getValue());
        c.addAllConnections(correct.getConnections());
      }
    }
     // Now all nodes, nodes connections, and nodes connections connections are good.
    
    return nodes;
  }
}
