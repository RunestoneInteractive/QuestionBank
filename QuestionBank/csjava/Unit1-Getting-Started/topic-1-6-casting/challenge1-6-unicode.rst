.. activecode:: challenge1-6-unicode
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-6-casting
   :topics: Unit1-Getting-Started/topic-1-6-casting
   :from_source: F
   :language: java

   Can you print out a letter from 3 different languages using this |Unicode Lookup| site?
   ~~~~
   public class ChallengeUnicode
   {
      public static void main(String[] args)
      {
        System.out.println("A in ASCII and Unicode is the decimal number 65: " + (char)65);
        System.out.println("You can typecast a decimal number to char for the Chinese character for sun: " + (char)11932);
        System.out.println("Or you can print out the Chinese character for moon using unicode hex: \u2E9D");


      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testChangedCode() {
            String origCode = "public class ChallengeUnicode {   public static void main(String[] args)   {     System.out.println(\"A in ASCII and Unicode is the decimal number 65: \" + (char)65);     System.out.println(\"You can typecast a decimal number to char for the Chinese character for sun: \" + (char)11932);     System.out.println(\"Or you can print out the Chinese character for moon using unicode hex: \\u2E9D\"); }  }";

            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }