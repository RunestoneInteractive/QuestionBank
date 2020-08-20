.. activecode:: lcdmtest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-6-DeMorgan
   :topics: Unit3-If-Statements/topic-3-6-DeMorgan
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.2355769231
   :total_students_attempting: 208
   :num_students_correct: 201.0
   :mean_clicks_to_correct: 1.776119403

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