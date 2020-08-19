.. activecode:: code2_7_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-7-string-methods
   :topics: Unit2-Using-Objects/topic-2-7-string-methods
   :from_source: T
   :language: java
   :practice: T
   :autograde: unittest

   This code contains some common mistakes with strings. Fix the code to use the string methods correctly.
   ~~~~
   public class StringMistakes
   {
      public static void main(String[] args)
      {
        String str1 = "Hello!";

        // Print out the first letter?
        System.out.println("The first letter in " + str1 + ":" + str1.substring(1,1) );

        // Print out the last character?
        System.out.println("The last char. in " + str1 + ":" + str1.substring(8) );

        // Print str1 in lower case? Will str1 change?
        str1.toLowerCase();
        System.out.println("In lowercase: " + str1);

      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "The first letter in Hello!:H\nThe last char. in Hello!:!\nIn lowercase: hello!";
            boolean passed = getResults(expect, output, "Expected output from main");
            assertTrue(passed);
        }
    }