.. activecode:: reverseString
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit4-Iteration
   :subchapter: topic-4-3-strings-loops
   :topics: Unit4-Iteration/topic-4-3-strings-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.2227722772
   :total_students_attempting: 202
   :num_students_correct: 183.0
   :mean_clicks_to_correct: 1.8196721311

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
            String origCode = "public class ReverseString\n{\n   public static void main(String[] args)\n   {\n     String s = \"Hello\";\n     String sReversed = \"\";\n     String ithLetter;\n\n     for(int i=0; i < s.length(); i++) {\n         ithLetter = s.substring(i,i+1);\n         // add the letter at index i to what's already reversed.\n         sReversed = ithLetter + sReversed;\n     }\n     System.out.println(s + \" reversed is \" + sReversed);\n   }\n }\n\n";
   
            boolean passed = codeChanged(origCode);
            assertTrue(passed);
        }
    }