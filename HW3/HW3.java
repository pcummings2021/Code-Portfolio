/*
 *  Author: Parker Cummings
 *  Email: pcummings2021@my.fit.edu
 *  Course: CSE 2010
 *  Section: 4
 * 
 *  Description of this program: This file takes two inputs, a list of data and a list of queueries. The first line is 
 *  the root of the tree, followed by it's children. The following lines are the children of those children, and so on. The root
 *  is the name of the event, followed by the sports, followed by the events, followed by the names and the countries of the 
 *  winners, including a Gold, Silver, and Bronze medals. The second input is a list of 8 possible queries, asking information
 *  about winners, countries, athletes, and the most gold and overallmedals. The queries are repeated in the output, along with the answer.
 */

// imports all necessary classes. ArrayList for the children, and Scanner and FileReader for taking input from the console
import java.util.Scanner;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;

// LinkedTree data structure which holds all the information in the given data
class LinkedTree {

    public treeNode root; // very first node in the tree, all nodes are children of this node, parent of root is null 
   
    static class treeNode implements Comparable<treeNode> { // implements Comparable interface for alphabetical order

        String data; // String to hold the event, sport, athlete, etc.
        treeNode parent; // every tree node has a parent except the root
        ArrayList<treeNode> children; // each node has a list of it's children, null for leaf nodes

        // constructs a node of the tree based on a String, data
        public treeNode (String d) { 
            this.data = d;
            this.parent = null;
            this.children = new ArrayList<treeNode>();
        }  
       
        // void method to add a node as a child of a parent node, takes a String the given data
        public void appendChild(String data) {
            treeNode newNode = new treeNode(data);
            newNode.parent = this;// sets the node using this method as the parent of the newNode
            this.children.add(newNode);
        }

        // void method to insert a child at a specific spot, to keep the alphabetical order
        public void insertChild(String data) {
            treeNode newNode = new treeNode(data);
            newNode.parent = this;
            for(int i = 0; i < this.children.size(); i++) {
                if(this.children.get(i).data.compareTo(data) < 1) { // finds the correct insertion point
                    this.children.add(i, newNode); // adds the node to the correct index
                }
            }
        }

        // compareTo method to sort a list of treeNodes alphabetically
        public int compareTo(treeNode node) { // takes in a treeNode, the node being compared
            if(this.data.compareTo(node.data) > 0) { // if node being compared is greater alphabetically
                return 1;
            }
            else if(this.data.compareTo(node.data) < 0) { // if node being compared is less alphabetically
                return -1;
            }
            else { // if they are equal
                return 0;
            }
        }
    }

    // adds a treeNode to a LinkedTree
    public void treeAdd(treeNode node, treeNode parent) {
        // if the parent of a node is null, it is a root node
        if(parent == null) {
            this.root = node;
        }
        else { 
            parent.children.add(node); // adds the node to the children of the parent
        }
    }

    // recursive search method, takes in a root node and a target, returns a node with data s
    public treeNode search(treeNode node, String s) {
        // if the node trying to be found is the root node
        if(node.data.equals(s)) { // base case for recursion
            return node;
        }
        else {
            // goes through all the children of every node, searching for the target node
            for(int i = 0; i < node.children.size(); i++) {
                treeNode newNode = search(node.children.get(i), s); //decompostion
                if(newNode != null) {
                    return newNode; // compostion
                }
            }
        }
        return null; // returns null if node does not exist in the tree
    }

    // for the "GetSportAndEventByAthlete" query
    public ArrayList<String> athleteSearch(treeNode node, String ath) {
        ArrayList<String> list = new ArrayList<>();
        ArrayList<treeNode> arr = addAllLeafs(this.root); // adds all treeNodes that are leafs to a list
        for(int i = 0; i < arr.size(); i++) {
            String[] arr2 = arr.get(i).data.split(":"); // splits the string by the colon to just get the athlete name
            if(arr2[0].equals(ath)) {
                // adds the sport and event of the given athlete to a string
                list.add(String.format("%s:%s", arr.get(i).parent.parent.data, arr.get(i).parent.data));
            }
        }
        return list; // returns the result
    }

    // recursive method that collects all leaf nodes into a list for comparison
    public ArrayList<treeNode> addAllLeafs(treeNode node) {
        ArrayList<treeNode> list = new ArrayList<>();
        // if the node is a leaf node
        if(node.children.isEmpty()) { // base case for recursion
            list.add(node); // compostion
        }
        else {
            // goes through all the children of every node
            for(int i = 0; i < node.children.size(); i++) {
                list.addAll(addAllLeafs(node.children.get(i))); //decompostion
            }
        }
        return list; // returns all leaf nodes 
    }

    // recursive method that collects either all athlete names or all country names for comparison
    public ArrayList<String> addAllLeafsForOneInfo(treeNode node, int index) {
        ArrayList<String> list = new ArrayList<>();
        // if the node is a leaf node
        if(node.children.isEmpty()) { // base case
            String[] str = node.data.split(":");
            list.add(str[index]); // compostion
        }
        else {
            // goes through all the children of every node
            for(int i = 0; i < node.children.size(); i++) {
                list.addAll(addAllLeafsForOneInfo(node.children.get(i), index)); //decompostion
            }
        }
        return list; // returns list of athlete names or country names, based on given index
    }

    // recursive method that collects all gold medalists' names or countries into a list for comparison
    public ArrayList<String> addAllGoldMedalists(treeNode node, int index) {
        ArrayList<String> list = new ArrayList<>();
        // if the node is a leaf node, add the gold medalist of that list
        if(node.children.isEmpty()) { // base case
            String[] str = node.parent.children.get(0).data.split(":");
            list.add(str[index]); // composition
        }
        else {
            // goes through all the children of every node
            for(int i = 0; i < node.children.size(); i++) {
                list.addAll(addAllGoldMedalists(node.children.get(i), index)); //decompostion
            }
        }
        return list; // returns result
    }

    /* void method to print all the elements in a tree, takes in a root node. String s can be used to seperate
       levels of the tree, can be " " or "-" or any other character, used for debugging */
    public static void printTree(treeNode node, String s) {
        System.out.println(s + node.data);
        for(int i = 0; i < node.children.size(); i++) {
            // decomposition, prints each level on a new column to the console
            printTree(node.children.get(i), s + s); // decompostion
        }

    }

    // void method for the "GetEventsBySport" query, takes in a String, the specified sport
    public void eventsBySport(String sport) {
        // finds the children nodes of the sport node
        ArrayList<treeNode> children = search(this.root, sport).children;
        Collections.sort(children);
        // prints all information to the console
        System.out.printf("%s %s ", "GetEventsBySport", sport);
        for(int i = 0; i < children.size(); i++) {
            // prints a new line if the list is at the final element
            if(i == children.size()-1) {
                System.out.printf("%s%n", children.get(i).data);
            }
            else {
                System.out.printf("%s ", children.get(i).data);
            }
        }
    }

    // void method for the "GetWinnersAndCountriesBySportAndEvent", takes in two strings, the sport and event
    public void winnersAndCountries (String sport, String event) {
        // gets a list of children of the event node
        ArrayList<treeNode> children = search(this.root, event).children;
        // prints all information to the console
        System.out.printf("%s %s %s ", "GetWinnersAndCountriesBySportAndEvent", sport, event);
        for(int i = 0; i < children.size(); i++) {
            if(i == children.size()-1) { // prints a new line if printing the last element
                System.out.printf("%s%n", children.get(i).data);
            }
            else { // prints elements
                System.out.printf("%s ", children.get(i).data);
            }
        }
    }

    // void method for "GetGoldMedalistAndCountryBySportAndEvent", takes in two strings, sport and event
    public void getGold(String sport, String event) {
        // gets the children of the event node, prints the first element, the gold winner
        treeNode child = search(this.root, sport);
        String goldWinner = search(child, event).children.get(0).data;
        System.out.printf("%s %s %s ", "GetGoldMedalistAndCountryBySportAndEvent", sport, event);
        System.out.printf("%s%n", goldWinner);
    }

    // void method for "GetAthleteWithMostMedals"
    public void mostMedals() {
        // attains list of all athletes and sorts the list
        ArrayList<String> list = this.addAllLeafsForOneInfo(this.root, 0); // index 0 to get athlete name
        Collections.sort(list);
        String str = this.findMaxOccurence(list);
        // prints the name and number of medals for the athlete with the highest frequency
        System.out.printf("%s %s%n", "GetAthleteWithMostMedals", str);
    }

    // void method for "GetAthleteWithMostGoldMedals"
    public void mostGold() {
        ArrayList<String> list = this.addAllGoldMedalists(this.root, 0); // index 0 to get athlete name
        Collections.sort(list);
        String str = this.findMaxOccurenceGold(list);
        // prints the name and # of gold medals for the athlete with the most gold medals
        System.out.printf("%s %s%n", "GetAthleteWithMostGoldMedals", str);
    }

    // void method for "GetCountryWithMostMedals"
    public void mostMedalsCountry() {
        ArrayList<String> list = this.addAllLeafsForOneInfo(this.root, 1); // index 1 to get country name
        Collections.sort(list); // maintains alphabetical order
        String str = this.findMaxOccurence(list); 
        // prints results to console
        System.out.printf("%s %s%n", "GetCountryWithMostMedals", str);
    }

    // void method for "GetCountryWithMostGoldMedals"
    public void mostGoldsCountry() {
        ArrayList<String> list = this.addAllGoldMedalists(this.root, 1); // index 1 to get country name
        Collections.sort(list);
        String str = this.findMaxOccurenceGold(list); // finds country with most gold medals
        // prints country with highest number of gold medals, and the number of gold medals
        System.out.printf("%s %s%n", "GetCountryWithMostGoldMedals", str);
    }
    

    // void method for the "GetSportAndEventByAthlete", takes in a String, the name of the athlete
    public void sportAndEvent(String athlete) {
        ArrayList<String> list = athleteSearch(this.root, athlete); // gets list of all sports an athlete competed in
        String str = "";
        for(int i = 0; i < list.size(); i++) { // adds all the sports and events to a string
            str += list.get(i);
            if(i != list.size()-1) {
                str += " "; // prints a space between all events and sports
            }
        }
        // prints results to console
        System.out.printf("%s %s %s%n", "GetSportAndEventByAthlete", athlete, str);
    }

    // method for finding the maximum # of occurences of winners, takes in a list of athlete names
    public String findMaxOccurence(ArrayList<String> list) {
        // initial values, sets the maximum to the first item in the list
        int count = 1;
        int max = 1;
        String currentMostMedals = list.get(0);
        String maxMostMedals = list.get(0);
        // loops through all remaining elements of list, compares to current max
        for(int i = 1; i < list.size(); i++) {
            if(currentMostMedals.equals(list.get(i))) { // tallies up the count for each element
                count++;
                if(max < count) { // sets the new max and maxElement to the current max and elements
                    max = count;
                    maxMostMedals = currentMostMedals;
                }
            }
            else {
                if(max < count) { // if the count is greater than the current max count, that element is the new max
                    max = count;
                    maxMostMedals = currentMostMedals;
                }
                currentMostMedals = list.get(i); // begins the next iteration
                count = 1;
            }
        }
        // combines the name and number for the data into a format String, returns the String
        String str = String.format("%s %s", String.valueOf(max), maxMostMedals);
        return str;
    }

    // method for finding the maximum # of occurences of gold winners, takes in a list of athlete names
    public String findMaxOccurenceGold(ArrayList<String> list) {
        // initial values, sets the maximum to the first item in the list
        int count = 1;
        int max = 1;
        String currentMostGold = list.get(0);
        String maxMostGold = list.get(0);
        // loops through all remaining elements of list, compares to current max
        for(int i = 1; i < list.size(); i++) {
            if(currentMostGold.equals(list.get(i))) { // tallies up the count for each element
                count++;
                if(count > max) {
                    max = count;
                    maxMostGold = currentMostGold;
                }
            }
            else {
                if(count > max) { // if the count is greater than the current max count, that element is the new max
                    max = count;
                    maxMostGold = currentMostGold;
                }
                currentMostGold = list.get(i); // begins the next iteration
                count = 1;
            }
        }
        // combines the name and number for the data into a format String, returns the String
        String str = String.format("%s %s", String.valueOf(max/3), maxMostGold);
        return str;
    }
}

// main class for the construction of the LinkedTree and the answers to the queries
public class HW3  {
    
    // buildTree method, builds a tree based on the given data, takes in a Scanner object for input
    public static LinkedTree buildTree(Scanner scan) {
        LinkedTree tree = new LinkedTree();
        String[] line = scan.nextLine().split(" "); // splits the line into an array of Strings
        // creates the root node and appends only the sports
        tree.root = new LinkedTree.treeNode(line[0]); 
        for(int i = 1; i < line.length; i++) {
            tree.root.appendChild(line[i]);
        }
        Collections.sort(tree.root.children);
        // continues to create nodes and append children for the sports and events
        while(scan.hasNextLine()) {
            String[] line1 = scan.nextLine().split(" ");
            LinkedTree.treeNode node = tree.search(tree.root, line1[0]);
            for(int i = 1; i < line1.length; i++) {
                node.appendChild(line1[i]);
            }
        }
        return tree; // returns the created tree
    }

    // void method to print answers to given queries, takes in a scanner and a tree
    public static void queries(Scanner scan1, LinkedTree tree) {
        while(scan1.hasNext()) {
            String event = scan1.next();
            // for the events query
            if(event.equals("GetEventsBySport")) {
                String sport = scan1.next();
                tree.eventsBySport(sport);
            }
            // for the winners and countries by sport query
            else if(event.equals("GetWinnersAndCountriesBySportAndEvent")) {
                String sport = scan1.next();
                String event1 = scan1.next();
                tree.winnersAndCountries(sport, event1);
            }
            // for the gold medalist query
            else if(event.equals("GetGoldMedalistAndCountryBySportAndEvent")) {
                String sport = scan1.next();
                String event1 = scan1.next();
                tree.getGold(sport, event1);
            }
            // for the athlete with the most medals query
            else if(event.equals("GetAthleteWithMostMedals")) {
                tree.mostMedals();
            }
            // for the athlete with the most gold medals query
            else if(event.equals("GetAthleteWithMostGoldMedals")) {
                tree.mostGold();
            }
            // for the country with the most medals query
            else if(event.equals("GetCountryWithMostMedals")) {
                tree.mostMedalsCountry();
            }
            // for the country with most gold medals query
            else if(event.equals("GetCountryWithMostGoldMedals")) {
                tree.mostGoldsCountry();
            }
            // for the get sport and event by athlete name event
            else if(event.equals("GetSportAndEventByAthlete")) {
                String athlete = scan1.next();
                tree.sportAndEvent(athlete);
            }
        }
    }
    
    // main method, takes in data and query text files, builds tree and answers query
    public static void main(String[] args) throws FileNotFoundException {
        String data = args[0]; // takes in the data
        String queries = args[1]; // takes in the queries
        Scanner scan = new Scanner(new FileReader(data)); // scanner for data
        Scanner scan1 = new Scanner(new FileReader(queries)); // scanner for queries
        LinkedTree tree = buildTree(scan); // builds tree on given data
        queries(scan1, tree); // answers all queries
    }
}
