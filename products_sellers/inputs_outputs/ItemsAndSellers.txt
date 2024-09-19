/*
 *  Author: Parker Cummings
 *  Email: pcummings2021@my.fit.edu
 *  Course: CSE 2010
 *  Section: 4
 * 
 *  Description of this program: This file takes three items: an iPhone, a HDMI to VGA Adapter, and a USB Drive.
 *  each item can has a price, a shipping cost, a quantity, and n number of sellers. They also CAN have a minimum cost for free shipping.
 *  There are 5 different events that can take place in the input. 'SetProductPrice', 'SetShippingCost', 'IncreaseInventory',
 *  'Customer Purchase', and 'DisplaySellerList'. There are two functions for each event. One to recognize the input, the other
 *  to perform the necessary operations. For each event, it is reprinted to the output and includes any additional information
 *  if it applies to the event. The 'DisplaySellerList' function returns a data table with the list of sellers for certain item.
 */

import java.util.Scanner; // imports the scanner class for recognizing input

/* LinkedList class to store a list of ordered Nodes */
class LinkedList {

    // Every LinkedList will start with a head and a tail, both set to null
    public Node head = null;
    public Node tail = null;
    
    // class Node to store data in the form of objects of the HW1 class
    static class Node {

        // Every Node will have data, an object, and next, a pointer to the following node
        HW1 data;
        Node next;

        public Node (HW1 d) { // a constructor for the Node class
            this.data = d;
            this.next = null;
        }  
    }

    /*
     *  creates and adds a node with the HW1 object to a specified list,
     *  takes in data, an object in the node of a LinkedList
     */ 
    public void add(HW1 data) {
        Node newNode = new Node(data); // creates a new node with the given data
        // Assigns the new node to the head position if the list is empty
        if(this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        }
        else { // else it will set the tail's next to the newNode, becoming the new tail
            this.tail.next = newNode;
            this.tail = newNode;
        }   
    }

    /* 
     *  finds a node with a specified seller in a specified list, 
     *  takes in a String s, the seller being searched for
     */
    public Node findSeller(String s) {
        Node current = this.head;
        while(current != null) {
            // returns the node with the specified seller
            if(current.data.seller.equals(s)) {
                return current; // returns the specific node once found
            }
            current = current.next;
        }
        return null; // returns an empty node if the a node with the seller is not found
    }

    /* 
     *  Checks a linkedList to see if a node with a specific seller already exists, 
     *  takes in a String s, the specified seller, as a parameter
     */
    public boolean checkForSeller(String s) {
        Node current = this.head; // used for traversal through the list
        while(current != null) {
            if(current.data.seller.equals(s)) {
                return true; // will return true if a node with the seller already exists
            }
            current = current.next;
        }
        return false; // return false if no nodes with the seller are found
    }

    // method to sort the linkedList in ascending order
    public void sortLinkedList() {
        HW1 tempItem = new HW1(); // a temporary object to hold the moving data
        Node current = this.head; // traverse through the list
        Node current2 = null; // initially set to null
        if(this.head == null) { // if the list is empty
            return;
        }
        else {
            while(current != null) { // will stop at the end of the list
                current2 = current.next;
                while(current2 != null) {
                    if(current.data.cost == current2.data.cost) {
                        // if the costs are the same, they are sorted alphabetically by seller
                        if(current.data.seller.compareTo(current2.data.seller) == 1) {
                            tempItem = current.data;
                            current.data = current2.data;
                            current2.data = tempItem;
                        }
                    }
                    // compares the costs of the two objects and sorts accordingly
                    if(current.data.cost > current2.data.cost) {
                        tempItem = current.data; // sets the data to the temporary object 
                        current.data = current2.data; // moves the nodes around
                        current2.data = tempItem; // sets the new node to the temporary data
                    }
                    current2 = current2.next;
                }
                current = current.next; // move along in the list
            }
        }
    }
    
    /* 
     *  Displays all of the sellers for a certain product, takes in 
     *  a LinkedList list, the specified list, and a String product, the item
     */
    public static void displaySellers(LinkedList list, String product) {
        HW1.setUpDisplay(); // sets up the base data table with the column headers
        Node current = list.head;
        while(current != null) {
            // adds the item cost and shipping cost and prints all the necessary information
            double totalCost = current.data.cost + current.data.shipCost; 
            // prints all of the sellers data to the console
            System.out.printf("%10s %14.2f %14.2f %11.2f%n", current.data.seller,
                    current.data.cost, current.data.shipCost, totalCost); 
            current = current.next;
        }
    }

    /*
     *  This method locates the node on the list with the specified product from
     *  the specified seller and changes the price to the new price given. The
     *  The method takes in a String n, the name, a String s, the seller, and a double
     *  c, the new cost
     */
    public void setPrice(String n, String s, double c) {
        HW1 item = new HW1(); // creates a new object based on the new data
        item.name = n;
        item.seller = s;
        item.cost = c;
        // if the list is empty or there is no node with the specified seller, add to the list
        if (this.head == null || !(this.checkForSeller(item.seller))) {
            this.add(item);
        }
        else {
            this.findSeller(item.seller).data.cost = c; // finds the node with a certain seller, changes cost
        }
        
    }

    /*
     *  Method incInventory to increase the certain inventory of a product for a certain seller,
     *  takes in the name of the item, the seller, and the quantity being added as parameters
     *  this method also returns the old quantity, to be printed to the console
     */ 
    public int incInventory(String product, String seller, int newQuantity){
        int oldQuantity = 0; // to keep track of the old quantity before the update
        LinkedList.Node current = this.head;
        while(current != null) {
            if(current.data.seller.equals(seller) && current.data.name.equals(product)) {
                // updates the quantity based on the given parameter
                oldQuantity = current.data.quantity;
                current.data.quantity += newQuantity;
            }
            current = current.next; // traverses the list
        }
        return oldQuantity; // returns the old quantity value
    }

    /*
     *  This method locates every node with a specified seller on a list
     *  and changes the cost of shipping in the node
     */
    public void setShip(String seller, double ship, double minFree) {
        Node current = this.head;  
        while(current != null) {
            // sets the shipCost to the parameter ship 
            if(current.data.seller.equals(seller)) {
                current.data.minForFree = minFree;
                // if the price of the item is greater than the minForFree, the shipCost is $0.00
                if(current.data.cost >= current.data.minForFree) {
                    current.data.shipCost = 0.0;
                }
                else { // if the price does not meet the minimum for free shipping
                    current.data.shipCost = ship;
                }
            }
            current = current.next;
        } 
    }

    /*  
     *  method for the 'CustomerPurchase' event, takes in the product name, seller, 
     *  and the quantity that the customer is purchasing. The method returns either 
     *  the updated quantity or "NotEnoughInventoryError" if there is not enough
     *  inventory to be purchased
     */
    public String customerPurch(String name, String seller, int quant) {
        Node current = this.head;
        while(current != null) {
            // finds the node with the correct seller and product name and updates the inventory
            if(current.data.seller.equals(seller) && current.data.name.equals(name)) {
                if(current.data.quantity >= quant) {
                    current.data.quantity -= quant;
                    return String.valueOf(current.data.quantity);
                }
                // if the new quantity is less than the current quantity, an error prints
                else { 
                    return "NotEnoughInventoryError";
                }
            }
            current = current.next;
        }
        return null; // if neither condition is met, a null string is returned
    }

    /*  a function to check if a specified seller's inventory is depleted,
     *  takes in a String s, the result of the purchaseEvent function, a
     *  String product, the name of the item, and a String seller
     */
    public void checkForDepleted(String s, String product, String seller) {
        if(!(s.equals("NotEnoughInventoryError"))) {
            if(Integer.parseInt(s) == 0) {
                // prints error to the console
                System.out.printf("%s %s %s%n", "DepletedInventoryRemoveSeller", product, seller);
            }
        }
    }
}
 
/*
 *  the class HW1 to store all the data. Every node's data will be a HW1
 *  object with the proper information for operation
 */
public class HW1 {

    // creates scanner object for recognizing input
    final static Scanner scan = new Scanner (System.in, "US-ASCII");

    // all the possible information an object could have based on the 5 events
    String name;
    String seller;
    double cost;
    double shipCost;
    double minForFree;
    int quantity;

    // no constructor, all values are originally set to their default values

    // creates the 3 LinkedLists for each of the three items
    static LinkedList iPhone = new LinkedList();
    static LinkedList hdmi = new LinkedList();
    static LinkedList usb = new LinkedList();

    // main method, one if statement for each of the 5 possible events
    public static void main(String[] args) {
        while(scan.hasNext()) {
            String event = scan.next();

            // for the SetProductPrice event 
            if(event.equals("SetProductPrice")) {
               priceEvent(event);
            }
            // for the SetShippingCost event
            else if(event.equals("SetShippingCost")) {
                shipEvent(event);
            }
            // for the IncreaseInventory event 
            else if(event.equals("IncreaseInventory")) {
                increaseEvent(event);
            }
            // for the CustomerPurchase event 
            else if(event.equals("CustomerPurchase")) {
                purchaseEvent(event);
            }
            // for the DisplaySellerList event 
            else if(event.equals("DisplaySellerList")) {
                displayEvent(event);
            }
        }
    }
    
    // function for calling the 'SetProductPrice' event
    public static void priceEvent(String event) {
        String product = scan.next();
        String sell = scan.next();
        double price = scan.nextDouble();
        // prints the event and information to the console
        if(price % 1 == 0) { // prints the price with no decimal if it is a whole number
            System.out.printf("%s %s %s %.0f%n", event, product, sell, price); 
        }
        else { // prints the price with 2 decimal places if it is not a whole number
            System.out.printf("%s %s %s %.2f%n", event, product, sell, price); 
        }
        // attempts all of the three possible items
        if(product.equals("appleIPhone")) { 
            iPhone.setPrice(product, sell, price);
        }
        else if(product.equals("hdmi2VgaAdapter")) {
            hdmi.setPrice(product, sell, price);
        }
        else if(product.equals("USBdrive")) {
            usb.setPrice(product, sell, price);
        }
    }

    // function for calling the 'SetShippingCost' event, takes in a string, the event
    public static void shipEvent(String event) {
        // scans in the necessary input for the operation 
        String seller = scan.next();
        double ship = scan.nextDouble();
        double minFree = scan.nextDouble();
        // prints information to the console before operation
        if(ship % 1 == 0) { // prints the shipping cost with no decimal if it is a whole number
            System.out.printf("%s %s %.0f %.0f%n", event, seller, ship, minFree); 
        }
        else { // prints the shipping cost with 2 decimal places if it is not a whole number
            System.out.printf("%s %s %.2f %.2f%n", event, seller, ship, minFree); 
        }
        iPhone.setShip(seller, ship, minFree);// executes operation for all three items for the seller
        hdmi.setShip(seller, ship, minFree);
        usb.setShip(seller, ship, minFree);
    }

    // a function for the 'IncreaseInventory' event, takes in a string, the event
    public static void increaseEvent(String event) {
        String product = scan.next();
        String sell = scan.next();
        int quantity = scan.nextInt();
        int newQuantity = 0; // the updated quantity
        // executes all operations
        if(product.equals("appleIPhone")) {
            newQuantity = iPhone.incInventory(product, sell, quantity);
        }
        else if(product.equals("hdmi2VgaAdapter")) {
            newQuantity = hdmi.incInventory(product, sell, quantity);
        }
        else if(product.equals("USBdrive")) {
            newQuantity = usb.incInventory(product, sell, quantity);
        }
        // prints all gathered information to the console, including the old and updated quantity
        System.out.printf("%s %s %s %d %d%n", event, product, sell, quantity, quantity + newQuantity);
    }

    // a function for the 'CustomerPurchase' event, takes in a string, the event
    public static void purchaseEvent(String event) {
        String product = scan.next();
        String sell = scan.next();
        int quantity = scan.nextInt();
        // a string s will either hold the updated quantity, or "NotEnoughtInventoryError"
        String s = "";
        // executes all operations
        if(product.equals("appleIPhone")) {
            s = iPhone.customerPurch(product, sell, quantity); 
            System.out.printf("%s %s %s %d %s%n", event, product, sell, quantity, s);
            // checks to make sure the inventory is not depleted after the purchase
            iPhone.checkForDepleted(s, product, sell);
        }
        else if(product.equals("hdmi2VgaAdapter")) {
            s =hdmi.customerPurch(product, sell, quantity);
            System.out.printf("%s %s %s %d %s%n", event, product, sell, quantity, s);
            hdmi.checkForDepleted(s, product, sell); 
        }
        else if(product.equals("USBdrive")) {
            s = usb.customerPurch(product, sell, quantity); 
            System.out.printf("%s %s %s %d %s%n", event, product, sell, quantity, s);
            hdmi.checkForDepleted(s, product, sell);
        }
    }
    
    // a function for the 'DisplaySellerList' event, takes in a string, the event
    public static void displayEvent(String event) {
        // scans in the item name and prints the event and name to the console
        String product = scan.next();
        System.out.printf("%s %s%n", event, product);
        // executes all operations and displays all seller information to the console
        if(product.equals("appleIPhone")) {
            iPhone.sortLinkedList();
            LinkedList.displaySellers(iPhone, product);
        }
        else if(product.equals("hdmi2VgaAdapter")) {
            hdmi.sortLinkedList();
            LinkedList.displaySellers(hdmi, product);
        }
        else if(product.equals("USBdrive")) {
            usb.sortLinkedList();
            LinkedList.displaySellers(usb, product);
        }
    }

    // a function to set up the basic data table for the seller list
    public static void setUpDisplay(){
        // prints all of the column headers in the correct spacing
        System.out.printf("%10s %14s %14s %11s%n", "seller", 
                "productPrice", "shippingCost", "totalCost");
    }
}
