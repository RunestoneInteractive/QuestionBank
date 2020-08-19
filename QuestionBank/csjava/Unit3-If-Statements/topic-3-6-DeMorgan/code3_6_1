.. activecode:: code3_6_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-6-DeMorgan
   :topics: Unit3-If-Statements/topic-3-6-DeMorgan
   :from_source: T
   :language: java
   :autograde: unittest

   For what values of x and y will the code below print true?  Try out different values of x and y to check your answer.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        int x = 2;
        int y = 3;
        System.out.println(!(x < 3 && y > 2));
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
            String origCode = "public class Test1 {public static void main(String[] args) { int x = 2; int y = 3; System.out.println(!(x < 3 && y > 2)); } }";

            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }