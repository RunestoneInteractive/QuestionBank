.. activecode:: imageArray
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit6-Arrays
   :subchapter: topic-6-1-array-basics
   :topics: Unit6-Arrays/topic-6-1-array-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.1111111111
   :total_students_attempting: 9
   :num_students_correct: 8.0
   :mean_clicks_to_correct: 2.375

   Can you change the index variable's value so that it prints out the puppy image? Can you print out the reindeer? Try all of them! What indices did you need to use? Then try using a random number for the index instead. Remember that (int)(Math.random()*max) will return a number from 0 up to max. What's the maximum number it can be for this array?
   ~~~~
   public class ImageEx
   {
    public static void main(String[] args)
    {
        String[] images = {"cow.jpg", "kitten.jpg",
                  "puppy.jpg", "pig.jpg", "reindeer.jpg"};
   
        ImageEx obj = new ImageEx();
        // Change index to see different images in the array!
        // Can you have it pick out a random image?
        int index = 0;
        obj.printHTMLimage( images[index] );
     }
   
     // This method will just work in Active Code which interprets html
     public void printHTMLimage(String filename)
     {
        String baseURL = "https://raw.githubusercontent.com/bhoffman0/CSAwesome/master/_sources/Unit6-Arrays/6-1-images/";
        System.out.print("<img src=" + baseURL + filename + ">");
      }
    }
    ====
    import static org.junit.Assert.*;
     import org.junit.*;;
     import java.io.*;
   
     public class RunestoneTests extends CodeTestHelper
     {
         @Test
         public void testCode()
         {
             String code = getCode();
             String expect = "int index = 0;";
   
             boolean passed = !code.contains(expect);
   
             getResults("index not 0",passed + "", "Changed index to another value", passed);
             assertTrue(passed);
         }
   
         @Test
         public void testRandomAdded() {
             boolean passed = checkCodeContains("Math.random to set index", "Math.random");
             assertTrue(passed);
         }
     }