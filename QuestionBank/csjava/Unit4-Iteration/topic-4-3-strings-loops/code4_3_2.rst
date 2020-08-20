.. activecode:: code4_3_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit4-Iteration
   :subchapter: topic-4-3-strings-loops
   :topics: Unit4-Iteration/topic-4-3-strings-loops
   :from_source: T
   :language: java
   :autograde: unittest

   What would happen if you started the loop at 1 instead? What would happen if you used <= instead of <? What would happen if you changed the order in which you added the ithLetter in line 12?
   ~~~~
   public class ReverseString
   {
      public static void main(String[] args)
      {
        String s = "Hello";
        String sReversed = "";
        String ithLetter;

        for(int i=0; i < s.length(); i++) {
            ithLetter = s.substring(i,i+1);
            // add the letter at index i to what's already reversed.
            sReversed = ithLetter + sReversed;
        }
        System.out.println(s + " reversed is " + sReversed);
      }
    }
    ====
    // Test for Lesson 4.3 - ReverseString
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ReverseString");
        }

        @Test
        public void testMain() throws IOException
        {
            String origCode = "public class ReverseString {    public static void main(String[] args)    {      String s = \"Hello\";      String sReversed = \"\";      String ithLetter;       for(int i=0; i < s.length(); i++) {          ithLetter = s.substring(i,i+1);          // add the letter at index i to what's already reversed.          sReversed = ithLetter + sReversed;      }      System.out.println(s + \" reversed is \" + sReversed);    }  }";

            boolean passed = codeChanged(origCode);
            assertTrue(passed);
        }
    }