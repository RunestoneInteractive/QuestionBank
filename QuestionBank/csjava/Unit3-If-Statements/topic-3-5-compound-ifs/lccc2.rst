.. activecode:: lccc2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: F
   :language: java
   :autograde: unittest

   For example, your parents might say you can go out if you can walk or they don't need the car.  Try different values for ``walking`` and ``carIsAvailable`` and see what the values have to be to print ``You can go out``.
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        boolean walking = false;
        boolean carIsAvailable = false;
        if (walking || carIsAvailable)
        {
           System.out.println("You can go out");
        }
        else
        {
          System.out.println("No, you can't go out");
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
            String origCode = "public class Test2 {public static void main(String[] args){boolean walking = false;boolean carIsAvailable = false;if (walking || carIsAvailable){System.out.println(\"You can go out\");}else{System.out.println(\"No, you can't go out\"); }}}";

            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
        @Test
        public void testMain() {
            String output = getMethodOutput("main");
           String expect = "You can go out";

           boolean passed = getResults(expect, output, "Expected output from main");
           assertTrue(passed);
        }
    }