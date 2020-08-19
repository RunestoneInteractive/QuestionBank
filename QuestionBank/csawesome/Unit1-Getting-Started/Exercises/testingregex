.. activecode:: testingregex
   :author: Linda Seiter
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: Exercises
   :topics: Unit1-Getting-Started/Exercises
   :from_source: F
   :language: java
   :autograde: unittest
   :pct_on_first: 0.0
   :total_students_attempting: 3
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 20.0

   lseiter testing countoccurrencesregex
   ~~~~
   public class TestRegex
   {
      public static void main(String[] args)
      {
        
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    public class RunestoneTests extends CodeTestHelper
    {
       public RunestoneTests() {
         super("TestRegex");
       }
   
   
       @Test
        public void test2()
        {
           String code = getCode();
           int sig = countOccurences(code, "public static void calculatePay(");
           boolean passed = sig == 1;
           passed = getResults("1 method signature", sig + " method signature", "Add a new method calculatePay", passed);
           assertTrue(passed);
        }
   
       @Test
        public void test3()
        {
           String code = getCode();
           int calls = countOccurences(code, "public static void calculatePay(");
           boolean passed = (calls==2);
           passed = getResults("2 calls", calls + " calls", "Update the main with two calls to calculatePay", passed);
           assertTrue(passed);
        }
   
   
    }