.. activecode:: code3_5_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: T
   :language: java
   :autograde: unittest

   The code below says if homework is not done, you can't go out. Try different values for ``homeworkDone``.
   ~~~~
   public class TestNot
   {    public static void main(String[] args)
      {
        boolean homeworkDone = false;
        if (!homeworkDone)
        {
            System.out.println("Sorry, you can't go out!");
        }
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
            String origCode = "public class TestNot{public static void main(String[] args){ boolean homeworkDone = false; if (!homeworkDone) { System.out.println(\"Sorry, you can't go out!\"); } } }";

            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
    }