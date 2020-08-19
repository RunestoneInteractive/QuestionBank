.. activecode:: lccc1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0724637681
   :total_students_attempting: 276
   :num_students_correct: 254.0
   :mean_clicks_to_correct: 2.2283464567

   What if you want to go out and your parents say you can go out if you clean your room and do your homework?  Run the code below and try different values for ``cleanedRoom`` and ``didHomework`` and see what they have to be for it to print ``You can go out``.
   ~~~~
   public class Test1
   {
      public static void main(String[] args)
      {
        boolean cleanedRoom = true;
        boolean didHomework = false;
        if (cleanedRoom && didHomework)
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
            String origCode = "public class Test1 { public static void main(String[] args){ boolean cleanedRoom = true; boolean didHomework = false; if (cleanedRoom && didHomework){ System.out.println(\"You can go out\");} else { System.out.println(\"No, you can't go out\");}}}";
   
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