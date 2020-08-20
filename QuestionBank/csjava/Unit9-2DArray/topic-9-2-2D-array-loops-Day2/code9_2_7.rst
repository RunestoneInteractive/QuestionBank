.. activecode:: code9_2_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: csjava
    :chapter: Unit9-2DArray
    :subchapter: topic-9-2-2D-array-loops-Day2
    :topics: Unit9-2DArray/topic-9-2-2D-array-loops-Day2
    :from_source: T
    :language: java
    :datafile: pictureClasses.jar, arch.jpg

    Picture Lab: write a method called zeroBlue() that sets the blue values at all pixels to zero. Continue on with other picture lab exercises as described below.
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

     /** switchColors() traverses the 2D pixel array and
      * switches the RGB colors.
      */
     public void switchColors()
     {
       Pixel[][] pixels = this.getPixels2D();
       int red, green, blue = 0;

       for (Pixel[] rowArray : pixels)
        {
          for (Pixel p: rowArray)
          {
           red = p.getRed();
           green = p.getGreen();
           blue = p.getBlue();
           p.setRed(green);
           p.setGreen(blue);
           p.setBlue(red);
         }
       }
     }

     /* Add new methods here.
        zeroBlue() method sets the blue values at all pixels to zero
     */

      /* Main method for testing
       */
      public static void main(String[] args)
      {
        Picture arch = new Picture("arch.jpg");
        arch.show();
        arch.switchColors();
        arch.show();

        //Uncomment the follow code to test your zeroBlue method.
        /*
        Picture arch2 = new Picture("arch.jpg");
        System.out.println("Zero blue: "); //using new method
        arch2.zeroBlue();
        arch2.show();
        */
        System.out.println();

        //Uncomment the follow code to test your keepOnlyBlue method.
        /*
        System.out.println("Keep only blue: ");
        arch.keepOnlyBlue();// using new method
        arch.show();
        */
      }
    }