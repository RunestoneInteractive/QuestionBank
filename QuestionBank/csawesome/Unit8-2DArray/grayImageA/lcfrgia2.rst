.. activecode:: lcfrgia2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: grayImageA
   :topics: Unit8-2DArray/grayImageA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.6
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.6

   FRQ Gray Image A: write the code for the method ``countWhitePixels``. When you are ready click "Run" to test your solution.
   ~~~~
   public class GrayImage
   {
      public static final int BLACK = 0;
      public static final int WHITE = 255;
   
      /** The 2-dimensional representation of this image.
       *  Guaranteed not to be null.
       *  All values in the array are within the range
       *  [BLACK, WHITE], inclusive.
       */
      private int[][] pixelValues;
   
      /** constructor that takes a 2D array */
      public GrayImage(int[][] theArray)
      {
         pixelValues = theArray;
      }
   
      /** @return the total number of white pixels in
       *    this image.
       * Postcondition: this image has not been changed.
       */
      public int countWhitePixels()
      {
   
      }
   
      /** main for testing */
      public static void main (String[] args)
      {
        int[][] values = { {255, 184, 178, 84, 129},
                          {84, 255, 255, 130, 94},
                          {78, 255, 0, 0, 78},
                          {84, 130, 255, 130, 84}};
        GrayImage image = new GrayImage(values);
        System.out.println("count white should be 5 and is " +
                           image.countWhitePixels());
      }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
     import java.util.List;
     import java.util.ArrayList;
   
     public class RunestoneTests extends CodeTestHelper
     {
   
       @Test
       public void testMain() throws IOException
       {
         String output = getMethodOutput("main");
         String expect = "count white should be 5 and is 5\n";
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
       @Test
       public void test1()
       {
         int[][] values = { {255, 255, 255},
                            {255, 255, 255},
                            {255, 255, 255}};
   
         GrayImage image = new GrayImage(values);
         String output = String.valueOf(image.countWhitePixels());
         String expect = "9";
   
         boolean passed = getResults(expect, output, "countWhitePixels 3X3, all are white");
         assertTrue(passed);
       }
   
       @Test
       public void test2()
       {
         int[][] values = { {255, 0},
                            {0, 255},
                            {255, 0},
                            {0, 255},};
   
         GrayImage image = new GrayImage(values);
         String output = String.valueOf(image.countWhitePixels());
         String expect = "4";
   
         boolean passed = getResults(expect, output, "countWhitePixels 4X2, half are white");
         assertTrue(passed);
       }
   
       @Test
       public void test3()
       {
         String code = getCode();
         String target = "for (int * = #;";
   
         int num = countOccurencesRegex(code, target);
   
         boolean passed = num == 2;
   
         getResults("2", ""+num, "2 For loops (nested)", passed);
         assertTrue(passed);
       }
     }