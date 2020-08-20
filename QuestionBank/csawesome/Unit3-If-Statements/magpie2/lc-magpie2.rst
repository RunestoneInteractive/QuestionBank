.. activecode:: lc-magpie2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: magpie2
   :topics: Unit3-If-Statements/magpie2
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.0

   Run to see the results. Try changing the input in main.
   ~~~~
   public class Magpie2
   {
      public String getGreeting()
      {
        return "Hello, let's talk.";
      }
   
      public String getResponse(String statement)
      {
        String response = "";
        if (statement.indexOf("no") >= 0) {
          response = "Why so negative?";
        } else if (statement.indexOf("mother") >= 0
                    || statement.indexOf("father") >= 0
                    || statement.indexOf("sister") >= 0
                    || statement.indexOf("brother") >= 0) {
          response = "Tell me more about your family.";
        } else {
          response = getRandomResponse();
        }
        return response;
      }
   
      private String getRandomResponse()
      {
        final int NUMBER_OF_RESPONSES = 4;
        double r = Math.random();
        int whichResponse = (int)(r * NUMBER_OF_RESPONSES);
        String response = "";
   
        if (whichResponse == 0) {
          response = "Interesting, tell me more.";
        } else if (whichResponse == 1) {
          response = "Hmmm.";
        } else if (whichResponse == 2) {
          response = "Do you really think so?";
        } else if (whichResponse == 3) {
          response = "You don't say.";
        }
        return response;
            }
   
      public static void main(String[] args)
      {
        Magpie2 maggie = new Magpie2();
   
        System.out.println(maggie.getGreeting());
        System.out.println(">My mother and I talked last night.");
        System.out.println(maggie.getResponse("My mother and I talked last night."));
        System.out.println(">I said no.");
        System.out.println(maggie.getResponse("I said no!"));
        System.out.println(">The weather is nice.");
        System.out.println(maggie.getResponse("The weather is nice."));
        System.out.println(">Do you know my brother?");
        System.out.println(maggie.getResponse("Do you know my brother?"));
      }
   }
   ====
    // should pass if/when they run code
    import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testMain() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "Hello, let's talk....";
            boolean passed = getResults(expect, output, "Expected output from main", true);
            assertTrue(passed);
        }
    }