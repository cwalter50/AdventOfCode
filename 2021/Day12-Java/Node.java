import java.util.List;
import java.util.ArrayList;

public class Node
{
    private ArrayList<Node> connections = null;
    // private List<Node> parents = null;
    private String value;
    private boolean isBig;

    public Node(String value)
    {
      this.connections = new ArrayList<Node>();
      this.value = value;
      isBig = this.value.equals(this.value.toUpperCase());
      
    }

    public ArrayList<Node> getConnections()
    {
      return this.connections;
    }

    public void addConnection(Node connection)
    {
      connections.add(connection);
    }
    public void addAllConnections(ArrayList<Node> c)
    {
      this.connections = c;
    }

    public String getValue()
    {
      return this.value;
    }

    public boolean isBig()
    {
      return isBig;
    }

    public boolean equals(Node other)
    {
      return this.value.equals(other.getValue());
    }

    public String toString()
    {
      return this.value;
      // String result = " ";
      // for (Node n: connections)
      //   result += n.getValue() + " ";
      // return this.value +":" +result;
    }

    
    

}
