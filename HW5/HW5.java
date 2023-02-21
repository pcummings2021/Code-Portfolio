/*
 *  Author: Parker Cummings
 *  Email: pcummings2021@my.fit.edu
 *  Course: CSE 2010
 *  Section: 4
 * 
 *  Description of this program: This program implements a skip list in order to simulate a wearable activity tracker. Users can
 *  add activities, including logging the time at which the activity was performed. Activites can be retrieved, given a time.
 *  Users can also remove activites from their tracker. Other functions include getting activites between two times, getting
 *  activites from earlier than a certain time in a certain day, or all activites in one day. There is also a function provided 
 *  to print the skip list. For the height of each tower in the list, the given class FakeRandHeight was provided.
 */

// imports all necessary classes, including scanner and file classes for reading input and Arraylist for an additional structure
import java.util.Scanner;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class HW5 {

    // main method for running the algorithm
    public static void main(String[] args) throws FileNotFoundException {
        // takes in the name of the text input file
        Scanner scan = new Scanner(new FileReader(args[0]));
        // calls the queries method to handle all the input
        queries(scan);
    }

    // void queries method to answer all queries provided by the input
    public static void queries(Scanner scan) {
        // creates in initially empty skiplist
        SkipList<SkipList.Node<Entry>> list = new SkipList<>();
        // loop continues until end of text file is found
        while(scan.hasNext()) {
            String event = scan.next();
            if(event.equals("AddActivity")) { // handles the adding of activites
                int time = scan.nextInt();
                String activity = scan.next();
                list = addActivity(list, time, activity); // scans input and calls add method
            }
            else if(event.equals("RemoveActivity")) { // handles the removal of activites
                int time = scan.nextInt();
                list = removeActivty(time, list); // scans input and calls remove method
            }
            else if(event.equals("GetActivity")) { // handles retrieval of activities
                int time = scan.nextInt();
                list = getActivity(time, list);
            }
            // handles the case in which the user wants all the activites between two given times
            else if(event.equals("GetActivitiesBetweenTimes")) {
                int startTime = scan.nextInt();
                int endTime = scan.nextInt();
                list = betweenTimes(startTime, endTime, list);
            }
            // handles the case in which user wants all the activities performed in one day
            else if(event.equals("GetActivitiesForOneDay")) {
                int date = scan.nextInt();
                list = oneDay(date, list);
            }
            // handles the case in which the user wants all activities performed before a certain time in the day
            else if(event.equals("GetActivitiesFromEarlierInTheDay")) {
                int currentTime = scan.nextInt();
                list = earlierInTheDay(currentTime, list);
            }
            // prints the entire skip list
            else if(event.equals("PrintSkipList")) {
                printSkipList(list);
            }
        }
    }

    // method for adding a activity to the skip list, takes in a (key, value) pair and a skip list
    public static SkipList<SkipList.Node<Entry>> addActivity(SkipList<SkipList.Node<Entry>> list, int time, String activity) {
        list.put(time, activity); // insertion
        // prints results to console
        System.out.printf("%s %d %s%n", "AddActivity", time, activity);
        return list;
    }
    
    // method for removing an activity from the skip list, takes in a key and a skip list
    public static SkipList<SkipList.Node<Entry>> removeActivty(int time, SkipList<SkipList.Node<Entry>> list) {
        SkipList.Node<Entry> n = list.remove(time); // removal
        String result = "";
        // prints "NoActivityError" if the key did not have a matching value in the skip list
        if(n == null) {
            result = "NoActivityError";
        }
        else {
            // sets the result string to the value of the removed node
            result = n.element.getValue();
        }
        // prints result to console
        System.out.printf("%s %d %s%n", "RemoveActivity", time, result);
        return list;
    }

    // method for retrieving a node, takes in a given key and a skip list
    public static SkipList<SkipList.Node<Entry>> getActivity(int time, SkipList<SkipList.Node<Entry>> list) {
        // uses the get function to retrieve the node
        SkipList.Node<Entry> n = list.get(time);
        // prints result to the console
        String result = n.element.getValue();
        // prints a NoActivtyError if the value is not found
        if(n.element.getValue() == null) {
            result = "None";
        }
        // prints result to console
        System.out.printf("%s %d %s%n", "GetActivity", time, result);
        return list;
    }

    // method for getting all activities between two given times, takes in start and end time, and a skip list
    public static SkipList<SkipList.Node<Entry>> betweenTimes(int startTime, int endTime, SkipList<SkipList.Node<Entry>> list) {
        // returns an arrray of all nodes with keys in between startTime and endTime
        ArrayList<SkipList.Node<Entry>> arr = list.subMap(startTime, endTime);
        // prints result to consoles
        System.out.printf("%s %d %d ", "GetActivitiesBetweenTimes", startTime, endTime);
        if(arr.size() == 0) {
            System.out.printf("%s", "None");
        }
        else {
            for(int i = 0; i < arr.size(); i++) {
                // prints each (key, value) pair to the console
                System.out.printf("%d:%s ", arr.get(i).element.getKey(), arr.get(i).element.getValue());
            }
        }
        System.out.printf("%n"); // prints a new line for the next query
        return list;
    }

    // method for retrieving all activities in a given day, takes in a date and a skip list
    public static SkipList<SkipList.Node<Entry>> oneDay(int time, SkipList<SkipList.Node<Entry>> list) {
        // additional data structure to hold activitiess
        ArrayList<SkipList.Node<Entry>> arr = new ArrayList<>();
        SkipList.Node<Entry> current = list.head; // starts from the beginning
        while(current.down != null) {
            current = current.down; // traverses down to the last level of the list, where all the nodes are located
        }
        current = current.next; // since the current node is negative infinity, we go to the next node
        while(current.next != null) {
            // since the input is only the 4 digit date, the date is extracted from each node
            String[] datesAndTimes = String.valueOf(current.element.key).split("");
            String date = "";
            // splits the key into each character and adds the first 3 to a new string
            for(int i = 0; i < 3; i++) {
                date = date + datesAndTimes[i]; // only adds 3 since the leading 0 is dropped
            }
            int dateAsInt = Integer.parseInt(date); // turns the result into an integer
            // checks if the dates match
            if(dateAsInt == time) {
                arr.add(current);
            }
            current = current.next; // iterates through the list
        }
        // prints the result to the console, including the key and value of every element
        System.out.printf("%s %d ", "GetActivitiesForOneDay", time);
        if(arr.size() == 0) {
            System.out.printf("%s", "None");
        }
        else {
            for(int i = 0; i < arr.size(); i++) {
                // prints each (key, value) pair to the console
                System.out.printf("%d:%s ", arr.get(i).element.getKey(), arr.get(i).element.getValue());
            }
        }
        System.out.printf("%n"); // prints a new line for the next query
        return list;
        
    }

    // method for retrieving all activities earlier than a certain time in the day
    public static SkipList<SkipList.Node<Entry>> earlierInTheDay(int currentTime, SkipList<SkipList.Node<Entry>> list) {
        // breaks down the current time into its date, since we need to make sure its only activities in that day
        String[] currentDate = String.valueOf(currentTime).split("");
        String cd = "";
        for(int i = 0; i < 3; i++) {
            cd = cd + currentDate[i]; // creates a string with the first 3 letters of the key, the date
        }
        int today = Integer.parseInt(cd); // creates an integer for the date of the currentTime
        ArrayList<SkipList.Node<Entry>> arr = new ArrayList<>(); // additional structure
        SkipList.Node<Entry> current = list.head; // starts at the head of the list
        while(current.down != null) {
            current = current.down; // traverses down to the lowest level where all nodes are located
        }
        current = current.next; // since the current node is negative infinity, we move to the next node
        while(current.next != null) {
            // splits the key to find the date for each node in the list, similar to above
            String[] datesAndTimes = String.valueOf(current.element.key).split("");
            String date = "";
            for(int i = 0; i < 3; i++) { // splits the key and adds the first three values, the date, to a new string
                date = date + datesAndTimes[i];
            }
            int dateAsInt = Integer.parseInt(date); // converts the string to an integer
            if(current.element.getKey() < currentTime && today == dateAsInt) {
                arr.add(current); // adds the node to the arrayList if it fits the conditions
            }
            current = current.next; // iterates through the list
        }
        // prints all information to the console
        System.out.printf("%s %01d ", "GetActivitiesFromEarlierInTheDay", currentTime);
        if(arr.size() == 0) {
            System.out.printf("%s", "None");
        }
        else {
            for(int i = 0; i < arr.size(); i++) {
                // prints each (key, value) pair to the console
                System.out.printf("%d:%s ", arr.get(i).element.getKey(), arr.get(i).element.getValue());
            }
        }
        System.out.printf("%n"); // prints a new line for the next query
        return list;
    }
    
    // method for printing the entire skip list
    public static void printSkipList(SkipList<SkipList.Node<Entry>> list) {
        System.out.printf("%s", "PrintSkipList");
        String s = String.format("");
        SkipList.Node<Entry> current = list.head; // the actual nodes of the list
        SkipList.Node<Entry> currentHead = list.head; // the head node on each level
        int currentLevel = list.height; // for printing (SX) where X is the current level of the skip list
        // iterates through each level
        while(currentHead != null) {
            // prints (S*level*) first
            s += ("\n(S" + currentLevel + ") ");
            // iterates through every node in each level
            while(current != null) {
                // will not print the head or tail nodes that have positive and negative infinity
                if(current.element.getValue() != null) {
                    // adds each key:value pair to the string
                    s += String.format("%d:%s ", current.element.getKey(), current.element.getValue());
                }
                // if the value is null, the node is checked to see if it is an empty level
                else if(current.next != null) {
                    // checks to see if the level is empty
                    if(checkForEmptyLevel(current)) {
                        s += "empty"; // adds string "empty" if the level has no activites
                    }
                }
                current = current.next; // iterates through each node in the current level
            }
            currentHead = currentHead.down; // moves down one level
            current = currentHead; // starts from the beginning of the level
            currentLevel--; // updates the current level
        }
        System.out.println(s); // prints the result
    }

    // static boolean method to see if a level is empty given a node
    public static boolean checkForEmptyLevel(SkipList.Node<Entry> node) {
        // checks if the current node is a negative infinity node and if the next is a positive infinity node
        if(node.element.getValue() == null && node.next.element.getValue() == null) {
            return true; // if the condition is true, the level is empty
        }
        return false; // if the condition fails, the level is not empty
    }
}
