/*
* Author: Parker Cummings, pcummings2021@my.fit.edu
* Course: CSE 1002, Section 3, Fall 2021
* Project: molecularweight
*/

import java.util.ArrayList;
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.Arrays;

public final class MolecularWeight {

   public record Entry (double weight, String equation, boolean isValid){

   }
   // boolean method to test if input is a number or not
   public static boolean isNumber (final String string) {
      try {
         final int num1 = Integer.parseInt(string);
         return true;
      }
      catch (final NumberFormatException e) {
         return false;
      }
   }

   public static void main (final String[] args) throws FileNotFoundException {

      // takes in .csv file for input
      final File input = new File ("elements.csv");

      // Creates scanner object SCAN for reading input from .csv file
      final Scanner SCAN = new Scanner (input, "US-ASCII");
      SCAN.useDelimiter(",");

      // Creates scanner object SCAN1 for reading input from command line
      final Scanner SCAN1 = new Scanner (System.in, "US-ASCII");
      SCAN1.useDelimiter(" ");

      // creates two different ArrayLists for holding all the names and
      // all the weights in the input elements.csv
      final ArrayList<String> names = new ArrayList<String>();
      final ArrayList<String> weights = new ArrayList<String>();
      while (SCAN.hasNextLine()) {
         final String[] arr = SCAN.nextLine().split(",");
         names.add(arr[2]);
         weights.add(arr[3]);
      }

      // Creates an ArrayList of Entry objects for each line of the Std input
      final ArrayList<Entry> entries = new ArrayList<Entry>();

      // Continues logic until no more tokens are found
      while (SCAN1.hasNext()) {

         // creates variables for the total weight, the final equation, and
         // the frequencey of an element
         double totalWeight = 0;
         String name = "";
         int freq = 0;

         // creates an array of strings with elements of each element or number
         // in the input
         final String in = SCAN1.nextLine();
         final ArrayList<String> symbols = new
               ArrayList<>(Arrays.asList(in.split(" ")));
         symbols.add("1");
         boolean isValid = true;
         // this for loop will test each value in the line of input
         for (int i = 0; i < symbols.size()-1; i++) {

            // adds the character to the final equation name
            name = name + symbols.get(i) + " ";

            double newWeight = 0;

            // will add the weight times the frequency to the total if the
            // input is a String and has a number following it
            if (!isNumber(symbols.get(i)) && isNumber(symbols.get(i+1))) {
               if (names.contains(symbols.get(i))) {
                  freq = Integer.parseInt(symbols.get(i+1));
                  newWeight = Double.parseDouble
                        (weights.get(names.indexOf(symbols.get(i))));
                  totalWeight += freq * newWeight;
               }
               else {
                  isValid = false;
                  totalWeight = 0;
               }
            }
            // will add the weight times 1 to the total if the input is a string
            // and is not followed by a number
            else if (!isNumber(symbols.get(i))) {
               if (names.contains(symbols.get(i))) {
                  newWeight = Double.parseDouble
                        (weights.get(names.indexOf(symbols.get(i))));
                  totalWeight += newWeight;
               }
               else {
                  isValid = false;
                  totalWeight = 0;
               }
            }


         }

         // create an Entry object with an equation name and total weight
         // add that Entry object to the ArrayList of entry objects
         final Entry newEntry = new Entry(totalWeight, name, isValid);
         entries.add(newEntry);
      }

      // prints all equations and weights in proper format
      for (int i = 0; i < entries.size(); i++) {

         // catches instance where equation is not valid
         if (!entries.get(i).isValid) {
            System.out.printf("Molecular weight of %s= %s%n",
                  entries.get(i).equation, "??");
         }
         else {
            System.out.printf("Molecular weight of %s= %.2f%n",
                  entries.get(i).equation, entries.get(i).weight);
         }
      }
   }
}
