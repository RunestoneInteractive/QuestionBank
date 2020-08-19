.. activecode:: nullTest
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-7-comparing-objects
   :topics: Unit3-If-Statements/topic-3-7-comparing-objects
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.4848484848
   :total_students_attempting: 165
   :num_students_correct: 152.0
   :mean_clicks_to_correct: 1.4934210526

   Try the following code to see a NullPointer error. Since s is null, indexOf throws an NullPointer error for s. Comment out the first if statement and run the program again. The second if statement avoids the error with shortcircuit evaluation. Because s != null is false, the rest of the boolean expression is not evaluated. Now, change s to set it to "apple" instead of null in the first line and run the code again to see that the if statements can print out that "apple contains an a".
   ~~~~
   public class NullTest
   {
      public static void main(String[] args)
      {
        String s = null;
        if (s.indexOf("a") >= 0)
        {
            System.out.println(s + " contains an a");
        }
        if (s != null && s.indexOf("a") >= 0)
        {
            System.out.println(s + " contains an a");
        }
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("NullTest");
        }
   
        @Test
        public void testMain() {
            String output = getMethodOutput("main");
            String expect = "apple contains an a\napple contains an a";
   
            boolean passed = getResults(expect, output, "Checking main() gives correct results");
        }
   
        @Test
        public void testChangedCode() {
            String origCode = "public class NullTest { public static void main(String[] args) { String s = null; if (s.indexOf(\"a\") >= 0) {  System.out.println(s + \" contains an a\"); } if (s != null && s.indexOf(\"a\") >= 0) { System.out.println(s + \" contains an a\"); } } }";
   
            boolean changed = codeChanged(origCode);
   
            assertTrue(changed);
   
        }
   
        @Test
        public void testCodeContains()
        {
            String code = getCode();
            String target1 = "String s = ";
            String target2 = "System.out.println(s + \" contains an a\");";
   
            boolean passed = code.contains(target1) && code.contains(target2);
            getResults("true", ""+passed, "Checking that code has not been removed", passed);
            assertTrue(passed);
        }
    }