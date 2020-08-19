.. activecode:: challenge2-7-PigLatin
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-7-string-methods
   :topics: Unit2-Using-Objects/topic-2-7-string-methods
   :from_source: F
   :language: java
   :practice: T
   :autograde: unittest

   Use the substring method to transform a word into Pig Latin where the first letter is put at the end and "ay" is added. The word pig is igpay in Pig Latin.
   ~~~~
   public class PigLatin
   {
      public static void main(String[] args)
      {
        String word =

        // Use word.substring to construct word in pig latin
        String pigLatin =

        System.out.println(word + " in Pig Latin is " + pigLatin);
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
            String expect = "* in Pig Latin is *ay";
            boolean passed = getResultsRegEx(expect, output, "Expected output from main");
            assertTrue(passed);
        }
       @Test
       public void testContainsSubstring()
       {
           String target = "word.substring(";
           int count = countOccurences(getCode(), target);
           boolean passed = count >= 2;
           passed = getResults("2 substring calls", count + " substring call(s)","Code contains calls to substring method", passed);
           assertTrue(passed);
       }
    }