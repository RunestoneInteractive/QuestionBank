.. activecode:: code2_6_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :language: java
   :autograde: unittest

   Here is an active code sample that creates two greeting strings: one using a string literal and the other using new
   and the String constructor. Change the code to add 2 new strings called firstName and lastName,
   one using a string literal and the other using new, and print them out with the greetings.
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
            String origCode = "public class StringTest {      public static void main(String[] args)      { String greeting1 = \"Hello!\";        String greeting2 = new String(\"Welcome!\");System.out.println(greeting1); System.out.println(greeting2); }    }";
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }