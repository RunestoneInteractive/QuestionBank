.. activecode:: ArrayListDeclare
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-1-arraylist-basics
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9850746269
   :total_students_attempting: 67
   :num_students_correct: 67.0
   :mean_clicks_to_correct: 1.0298507463

   In the code below we are declaring a variable called ``nameList`` that can refer to a ArrayList of strings, but currently doesn't refer to any ArrayList yet (it's set to ``null``).
   ~~~~
   import java.util.*; // import for ArrayList
   
   public class ArrayListDeclare
   {
       public static void main(String[] args)
       {
          ArrayList<String> nameList = null;
          System.out.println(nameList);
       }
    }
    ====
    import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("ArrayListDeclare");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "null";
   
            boolean passed = getResults(expect, output, "main()", true);
            assertTrue(passed);
        }
   
    }