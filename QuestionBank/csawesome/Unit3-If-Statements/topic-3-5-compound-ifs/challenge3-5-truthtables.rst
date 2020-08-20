.. activecode:: challenge3-5-truthtables
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-5-compound-ifs
   :topics: Unit3-If-Statements/topic-3-5-compound-ifs
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.2947368421
   :total_students_attempting: 190
   :num_students_correct: 139.0
   :mean_clicks_to_correct: 3.2589928058

   Challenge-3-5-truthtables: Test your boolean expression in an if statement below.
   ~~~
   public class TruthTable
   {
      public static void main(String[] args)
      {
          // Test multiple values for these variables
          boolean sunny = false;
          int temperature = 90;
          boolean raining = false;
   
          // Write an if statement for: If it's sunny,
          //  OR if the temperature is greater than 80
          //     and it's not raining, "Go to the beach!"
   
   
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
          String expect = "Go to the beach!";
          String output = getMethodOutput("main");
          String code = getCode();
          boolean passed;
          if (getCode().contains("boolean sunny = false"))
             passed = getResults(expect, output, "Prints Go to the beach! with initial input (sunny = false; temperature = 90; raining = false;)");
          else
            passed = getResults("sunny = false","sunny = true", "Set sunny to false to test");
   
          assertTrue(passed);
        }
   
        @Test
        public void testCodeContains1(){
          boolean ifStatement = checkCodeContains("conditional: if", "if");
          assertTrue(ifStatement);
        }
   
        @Test
        public void testCodeContains2(){
          boolean ifStatement1 = checkCodeContains("conditional: temperature greater than 80", "temperature > 80");
   
          assertTrue(ifStatement1);
        }
   
         @Test
        public void testCodeContains4(){
          boolean ifStatement3 = checkCodeContains("and", "&&");
          assertTrue(ifStatement3);
        }
        @Test
        public void testCodeContains5(){
          boolean ifStatement3 = checkCodeContains("or", "||");
          assertTrue(ifStatement3);
        }
    }