.. activecode:: frq2019Q3A-delim
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: 2019delimitersQ3a
   :topics: Unit7-ArrayList/2019delimitersQ3a
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.8
   :total_students_attempting: 5
   :num_students_correct: 5.0
   :mean_clicks_to_correct: 1.4

   Write the method getDelimitersList in the code below. The main method contains code to test your solution.
   ~~~~
   import java.util.*;
   public class Delimiters
   {
   
       /** The open and close delimiters **/
       private String openDel;
       private String closeDel;
   
       /** Constructs a Delimiters object were open is the open delimiter and close is the
        *  close delimiter.
        *  Precondition: open and close are non-empty strings
        */
       public Delimiters (String open, String close)
       {
           openDel = open;
           closeDel = close;
       }
   
       /** Returns an ArrayList of delimiters from the array tokens, as described in part (a). */
       public ArrayList<String> getDelimitersList(String[] tokens)
       {
           /* to be implemented in part a */
       }
   
       public static void main(String[] args)
       {
           Delimiters d1 = new Delimiters("(", ")");
           String[] tokens = {"(", "x + y", ")", " * 5" };
           ArrayList<String> res1 = d1.getDelimitersList(tokens);
           System.out.println("It should print [(, )] and it prints" + res1);
   
           Delimiters d2 = new Delimiters("<q>", "</q>");
           String[] tokens2 = {"<q>", "yy", "</q>", "zz", "</q>"};
           ArrayList<String> res2 = d2.getDelimitersList(tokens2);
           System.out.println("It should print [<q>, </q>, </q>] and it prints " + res2);
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
    import java.util.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
       @Test
      public void testRunGetDelimitersList()
      {
          Delimiters d1 = new Delimiters("[", "]");
          String[] tokens = {"[", "[", "x", "]", "]", "+ 5" };
          ArrayList<String> res1 = d1.getDelimitersList(tokens);
          String[] answer = {"[", "[", "]", "]" };
          List<String> answerList = Arrays.asList(answer);
          boolean passed = res1.equals(answerList);
          getResults("true", passed+"","getDelimitersList(\"{[[x]]+5})", passed);
          assertTrue(passed);
      }
   
     @Test
     public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "It should print [(, )] and it prints[(, )]\nIt should print [<q>, </q>, </q>] and it prints [<q>, </q>, </q>]\n";
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
   
      @Test
      public void checkCodeContains1()
      {
        //check accessor method getDelimitersList()
        boolean passed = checkCodeContains("correct getDelimitersList method header", "ArrayList<String> getDelimitersList(String[]");
        assertTrue(passed);
   
      }
   
     @Test
      public void checkCodeContains2()
      {
        //check accessor method getDelimitersList() creates a new ArrayList<String>
        boolean passed = checkCodeContains("new ArrayList<String> declared in method","= new ArrayList<String>()");
        assertTrue(passed);
      }
   
       @Test
      public void checkCodeContains3()
      {
        //check accessor method getDelimtersList() checks for open delimiters in generating returned delimitaor ArrayList
        boolean passed = checkCodeContains("checks for open delimiters",".equals(openDel)");
        assertTrue(passed);
      }
   
       @Test
      public void checkCodeContains4()
      {
        //check accessor method getDelimtersList() checks for close delimiters in generating returned delimitaor ArrayList
        boolean passed = checkCodeContains("checks for closed delimiters",".equals(closeDel)");
        assertTrue(passed);
      }
    }