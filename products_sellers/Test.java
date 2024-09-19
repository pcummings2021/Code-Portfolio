public class Test {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        LinkedList.Node newNode1 = new Node();
        newNode1.data = 1;
        LinkedList.Node newNode2 = new Node();
        newNode2.data = 2;
        LinkedList.Node newNode3 = new Node();
        newNode4.data = 3;
        LinkedList.Node newNode4 = new Node();
        newNode4.data = 4;
        LinkedList.add(list, newNode1);
        LinkedList.add(list, newNode2);
        LinkedList.add(list, newNode3);
        LinkedList.add(list, newNode4);
        LinkedList.Node myNode = list.head;
        while(myNode.next != null) {
            System.out.print(myNode.data);
            myNode = myNode.next;
        }
        
    }
}
class LinkedList1 {

        public Node1 head = null;
        public Node1 tail = null;
        
    
        static class Node1 {
    
            int data;
            Node1 next;
    
            public Node1 (int d) {
                this.data = d;
                this.next = null;
            }  
            
    
        }
        /*
        This add method takes in a LinkedList and an object as
        parameters and adds the object to the list.
         */
        public static void add(LinkedList1 list, int data) {
            
            Node1 newNode = new Node1(data);
    
            if(list.head == null) {
                list.head = newNode;
                list.tail = newNode;
            }
            else { 
                list.tail.next = newNode;
                list.tail = newNode;
            }   
        }
       /* finds a node with a specified seller in a specified list */
        public static Node1 findNumber(LinkedList1 list, int find) {
            Node1 current = list.head;
            while(current.next != null) {
                if(current.data == find) {
                    return current;
                }
                current = current.next;
            }
            return null;
        }
    }
