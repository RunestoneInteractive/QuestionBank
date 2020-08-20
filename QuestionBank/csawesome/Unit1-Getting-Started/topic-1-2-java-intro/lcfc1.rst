.. activecode:: lcfc1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-2-java-intro
   :topics: Unit1-Getting-Started/topic-1-2-java-intro
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.9961592179
   :total_students_attempting: 2864
   :num_students_correct: 2864.0
   :mean_clicks_to_correct: 1.0038407821

   Run this code to see the output below it. Then change the code to print your name, for example "Hi Pat!", and run again.
   ~~~~
   public class MyClass
   {
      public static void main(String[] args)
      {
          System.out.println("Hi there!");
      }
   }
   
   ====
   // should pass if/when they run code
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;
   
   public class RunestoneTests extends CodeTestHelper
   {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Hi there!";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
   }