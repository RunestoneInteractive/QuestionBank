.. activecode:: lcsb2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-6-strings
   :topics: Unit2-Using-Objects/topic-2-6-strings
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9965277778
   :total_students_attempting: 288
   :num_students_correct: 288.0
   :mean_clicks_to_correct: 1.0034722222

   Now that greeting refers to an actual object we can ask the object what class created it. Try the following.  What does it print?
   ~~~~
   public class Test2
   {
      public static void main(String[] args)
      {
        String greeting = "Hello";
        Class currClass = greeting.getClass();
        System.out.println(currClass);
        Class parentClass = currClass.getSuperclass();
        System.out.println(parentClass);
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "class java.lang.String\nclass java.lang.Object";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }