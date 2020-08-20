.. activecode:: NumberGroupB
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: FreeResponse
   :subchapter: NumberGroupB
   :topics: FreeResponse/NumberGroupB
   :from_source: T
   :language: java

   class NumberGroup
   {
      /* Implementation not shown */
   }

   public class Range extends NumberGroup
   {
       //Write the instance variables for the Range class here

       // Write the Range constructor with 2 parameters
       // for the minimum and maximum values in the range


       // Write the contains method which tests whether a
       // given number is in the range.

       //Main method to test the class
       public static void main(String[] args)
       {
           System.out.println("This is testing the constructor");
           Range test = new Range(5, 8);
           // Test the contains method
           System.out.println("Does the range contain 4 (should be false): " + test.contains(4));
           System.out.println("Does the range contain 5 (should be true): " + test.contains(5));

       } // end of main

   } // end of class