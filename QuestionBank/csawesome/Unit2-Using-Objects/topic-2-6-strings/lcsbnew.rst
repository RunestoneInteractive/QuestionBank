.. activecode:: lcsbnew
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.654109589
   :total_students_attempting: 292
   :num_students_correct: 273.0
   :mean_clicks_to_correct: 1.3186813187

   Here is an active code sample that creates two greeting strings: one using a string literal and the other using new and the String constructor. Change the code to add 2 new strings called firstname and lastname, one using a string literal and the other using new, and print them out with the greetings.
   ~~~~
   public class StringTest
   {
      public static void main(String[] args)
      {
          String greeting1 = "Hello!";
          String greeting2 = new String("Welcome!");
          System.out.println(greeting1);
          System.out.println(greeting2);
       }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testChangedCode() {
            String origCode = "public class StringTest {      public static void main(String[] args)      { String greeting1 = \"Hello!\";        String greeting2 = new String(\"Welcome!\"); System.out.println(greeting1); System.out.println(greeting2); }    }";
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }