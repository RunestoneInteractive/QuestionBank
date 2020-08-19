.. activecode:: lcfrgib4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit8-2DArray
   :subchapter: grayImageB
   :topics: Unit8-2DArray/grayImageB
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.25
   :total_students_attempting: 4
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 3.0

   FRQ Gray Image B: write the code for the method ``processImage``.
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
   
      /** Processes this image in row-major order and
       *  decreases the value of each pixel at position (row, col)
       *  by the value of the pixel at position (row + 2, col + 2)
       *  if it exists.
       * Resulting values that would be less than BLACK are replaced
       *   by BLACK.
       * Pixels for which there is no pixel at
       *   position (row + 2, col + 2) are unchanged.
       */
      public void processImage()
      {
   
      }
   
      public void printValues()
      {
        for (int r = 0; r < pixelValues.length; r++)
        {
          for (int c = 0; c < pixelValues[0].length; c++)
          {
            System.out.print(pixelValues[r][c] + ", ");
          }
          System.out.println();
        }
      }
   
      /** main for testing */
      public static void main (String[] args)
      {
        int[][] values = { {221, 184, 178, 84, 135},
                          {84, 255, 255, 130, 84},
                          {78, 255, 0, 0, 78},
                          {84, 130, 255, 130, 84}};
        GrayImage image = new GrayImage(values);
        image.printValues();
        image.processImage();
        System.out.println("after process image");
        image.printValues();
      }
   }
   ====
   import static org.junit.Assert.*;
     import org.junit.*;
     import java.io.*;
     import java.util.List;
     import java.util.ArrayList;
     import java.util.Arrays;
   
     public class RunestoneTests extends CodeTestHelper
     {
   
       @Test
       public void testMain() throws IOException
       {
         String output = getMethodOutput("main");
         String expect = "221, 184, 178, 84, 135,\n" +
                         "84, 255, 255, 130, 84,\n" +
                         "78, 255, 0, 0, 78,\n" +
                         "84, 130, 255, 130, 84,\n" +
                         "after process image\n" +
                         "221, 184, 100, 84, 135,\n" +
                         "0, 125, 171, 130, 84,\n" +
                         "78, 255, 0, 0, 78,\n" +
                         "84, 130, 255, 130, 84,\n" ;
   
         boolean passed = getResults(expect, output, "Expected output from main");
         assertTrue(passed);
       }
   
     @Test
       public void test1()
       {
         String target = "pixelValues[row+2][col+2];";
         boolean passed = checkCodeContainsRegex("altered pixel value",target);
         assertTrue(passed);
       }
   
     @Test
     public void test2()
       {
         String target1 = "pixelValues[row][col] < BLACK";
         String target2 = "pixelValues[row][col] < 0";
   
         boolean passed = checkCodeContainsRegex("check of pixel value less than 0",target1) ||                       checkCodeContainsRegex("check of pixel value less than 0",target2);
         assertTrue(passed);
       }
     }