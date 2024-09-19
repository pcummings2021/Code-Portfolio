/*
 * Author: Parker Cummings, pcummings2021@my.fit.edu
 * Course: CSE 1002, Section 3, Fall 2021
 * Project: walk
 */

import java.util.Random; // imports random class for RNG number

public final class RandomWalker { // creates RandomWalker Class
   private static final Random RNG =
         new Random (Long.getLong ("seed", System.nanoTime()));
   // creates random class for creating random objects
   public static void main (final String[] args) {

      final Integer n = Integer.parseInt(args[0]); // input n steps
      final Integer t = Integer.parseInt(args[1]); // input t trials

      Integer xPos = 0; // creates variable for x position on grid
      Integer yPos = 0; // creates variable for y position on grid
      double dist = 0.0; // variable for the 2D Euclidean distance
      int r = 0; // variable for the RNG number for one step
      int og = 0; // counter for times particle ends where it begins

      for (int i = 0; i < t; i++) { // loops through t trials
         for (int j = 0; j < n; j++) { // loops through n steps
            r = RNG.nextInt(4); // creates a random integer from 0-3
            if (r == 0) {
               xPos++; // will move particle 1 unit East if r = 0
            }
            else if (r == 1) {
               yPos++; // will move particle 1 unit North if r = 1
            }
            else if (r == 2) {
               xPos--; // will move particle 1 unit West if r = 2
            }
            else if (r == 3) {
               yPos--; // will move particle 1 unit South if r = 3
            }
         }
         dist += (Math.hypot(xPos, yPos)); /* adds 2D Euclidean distance
                                              to a total variable */
         if (0 == xPos && 0 == yPos) {
            og++; // adds one if particle ends where it began
         }
         xPos = 0; // resets x position before next trial
         yPos = 0; // resets y position before next trial
      }
      dist /= t; // returns average 2D Euclidean distance
      System.out.printf("%d %.2f%n", og, dist); // prints results
   }
}
