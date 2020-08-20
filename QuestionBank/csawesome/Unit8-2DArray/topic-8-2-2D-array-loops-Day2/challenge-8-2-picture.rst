.. activecode:: challenge-8-2-picture
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit8-2DArray
    :subchapter: topic-8-2-2D-array-loops-Day2
    :topics: Unit8-2DArray/topic-8-2-2D-array-loops-Day2
    :from_source: T
    :language: java
    :autograde: unittest
    :datafile: pictureClasses.jar, arch.jpg
    :pct_on_first: 0.1162790698
    :total_students_attempting: 43
    :num_students_correct: 25.0
    :mean_clicks_to_correct: 3.24

    Picture Lab: 1) write a method called keepOnlyBlue() that keeps only the blue values by setting the red and green values to zero. Uncomment the code in main to test it. 2) write a method called switchColors() that replaces red values (using p.setRed) with green or blue values (using p.getGreen(), etc.) to change the colors around. Uncomment the code in main to test it.
    ~~~~
    import java.awt.*;
    import java.awt.font.*;
    import java.awt.geom.*;
    import java.awt.image.BufferedImage;
    import java.text.*;
    import java.util.*;
    import java.util.List;
    
    /**
     * A class that represents a picture.  This class inherits from
     * SimplePicture and allows the student to add functionality to
     * the Picture class.
     *
     * @author Barbara Ericson ericson@cc.gatech.edu
     */
    public class Picture extends SimplePicture
    {
      ///////////////////// constructors //////////////////////////////////
    
      /**
       * Constructor that takes no arguments
       */
      public Picture ()
      {
        /* not needed but use it to show students the implicit call to super()
         * child constructors always call a parent constructor
         */
        super();
      }
    
      /**
       * Constructor that takes a file name and creates the picture
       * @param fileName the name of the file to create the picture from
       */
      public Picture(String fileName)
      {
        // let the parent class handle this fileName
        super(fileName);
      }
    
      /**
       * Constructor that takes the height and width
       * @param height the height of the desired picture
       * @param width the width of the desired picture
       */
      public Picture(int height, int width)
      {
        // let the parent class handle this width and height
        super(width,height);
      }
    
      /**
       * Constructor that takes a picture and creates a
       * copy of that picture
       * @param copyPicture the picture to copy
       */
      public Picture(Picture copyPicture)
      {
        // let the parent class do the copy
        super(copyPicture);
      }
    
      /**
       * Constructor that takes a buffered image
       * @param image the buffered image to use
       */
      public Picture(BufferedImage image)
      {
        super(image);
      }
      ////////////////////// methods ///////////////////////////////////////
    
      /**
       * Method to return a string with information about this picture.
       * @return a string with information about the picture such as fileName,
       * height and width.
       */
      public String toString()
      {
        String output = "Picture, filename " + getFileName() +
          " height " + getHeight()
          + " width " + getWidth();
        return output;
    
      }
    
      /**
        zeroBlue() method sets the blue values at all pixels to zero
     */
      public void zeroBlue()
      {
        Pixel[][] pixels = this.getPixels2D();
    
        for (Pixel[] rowArray : pixels)
         {
           for (Pixel p: rowArray)
           {
                  p.setBlue(0);
           }
        }
      }
    
    
     /* Add new methods here.
        keepOnlyBlue() method sets the blue values at all pixels to zero.
        switchColors() method swaps the color values of pixels.
     */
    
      /* Main method for testing
       */
      public static void main(String[] args)
      {
        Picture arch = new Picture("arch.jpg");
        arch.show();
        arch.zeroBlue();
        arch.show();
    
        //Uncomment the follow code to test your keepOnlyBlue method.
        /*
        Picture arch2 = new Picture("arch.jpg");
        System.out.println("Keep only blue: ");
        arch2.keepOnlyBlue();// using new method
        arch2.show();
        */
        System.out.println();
    
        //Uncomment the follow code to test your swithColors method.
        /*
        Picture arch3 = new Picture("arch.jpg");
        System.out.println("Switch colors: ");
        arch3.switchColors();// using new method
        arch3.show();
        */
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
       public void test1()
       {
         String target = "public void keepOnlyBlue()";
         boolean passed = checkCodeContains("keepOnlyBlue() method",target);
         assertTrue(passed);
       }
    
       @Test
       public void test2()
       {
         String target = ".setGreen(0);";
         boolean passed = checkCodeContains("keepOnlyBlue() setting green pixels to the number 0",target);
         assertTrue(passed);
       }
    
       @Test
         public void test3()
         {
             String target = "for";
             String code = getCode();
             int index = code.indexOf("public void keepOnlyBlue()");
             code = code.substring(index, index + 200);
             boolean passed = code.contains(target);
    
             getResults("true", ""+passed, "Checking that keepOnlyBlue() contains 2 for loops", passed);
             assertTrue(passed);
         }
         @Test
        public void testSwitch1()
        {
         String target = "public void switchColors()";
         boolean passed = checkCodeContains("switchColors() method",target);
         assertTrue(passed);
        }
    
        @Test
        public void testSwitch2()
        {
         String target = ".getGreen();";
         boolean passed = checkCodeContains("switchColors() uses getGreen()",target);
         assertTrue(passed);
        }
      }