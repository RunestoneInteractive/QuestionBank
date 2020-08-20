.. activecode:: lc-strEx
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: magpie3
   :topics: Unit3-If-Statements/magpie3
   :from_source: T
   :language: java
   :autograde: unittest

   Run the code below. Why do you think you might want to change the string to all lowercase characters? Why doesn't the value of ``sample`` change? Do string methods change the string? Try some other string methods.
   ~~~~
   /**
    * A program to allow students to try out different
    * String methods.
    * @author Laurie White
    * @version April 2012
    */
   public class StringExplorer
   {

      public static void main(String[] args)
          {
             String sample = "The quick brown fox jumped over the lazy dog.";

                 //  Demonstrate the indexOf method.
                 int position = sample.indexOf("quick");
                 System.out.println ("sample.indexOf(\"quick\") = " + position);

                 //  Demonstrate the toLowerCase method.
                 String lowerCase = sample.toLowerCase();
                 System.out.println ("sample.toLowerCase() = " + lowerCase);
                 System.out.println ("After toLowerCase(), sample = " + sample);

                 //  Try other methods here:

         }
   }
   ====
   // should pass if/when they run code
    import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "sample.indexOf("quick") = 4\n...";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }