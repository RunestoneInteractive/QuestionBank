.. activecode:: challenge3-6-booleanExpr
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-6-DeMorgan
   :topics: Unit3-If-Statements/topic-3-6-DeMorgan
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.3157894737
   :total_students_attempting: 152
   :num_students_correct: 112.0
   :mean_clicks_to_correct: 2.4553571429

   Are these 3 boolean expressions equivalent? 1. !(x == 0 || x >= 1) , 2. !(x == 0) && !(x >= 1) , 3. (x != 0) && (x < 1)
   ~~~~
   public class EquivalentExpressions
   {
      public static void main(String[] args)
      {
          int x = -1; // try with x = -1, x = 0, and x = 1
          System.out.println(!(x == 0 || x >= 1));
          // add print statements for expressions in #2 and #3
          // to see if they are equivalent when x = -1, 0, and 1.
   
   
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
             String origCode = "public class EquivalentExpressions { public static void main(String[] args) { int x = -1;  System.out.println(!(x == 0 || x >= 1));   } }";
   
            boolean changed = codeChanged(origCode);
            assertTrue(changed);
        }
   
      @Test
      public void testAddedCode(){
        boolean output2 = checkCodeContains("(x != 0) && (x < 1)");
        assertTrue(output2);
      }
   
      @Test
      public void testAddedCode2(){
        boolean output3 = checkCodeContains("!(x == 0) && !(x >= 1)");
        assertTrue(output3);
      }
    }