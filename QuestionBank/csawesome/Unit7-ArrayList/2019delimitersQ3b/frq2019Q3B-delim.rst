.. activecode:: frq2019Q3B-delim
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: 2019delimitersQ3b
   :topics: Unit7-ArrayList/2019delimitersQ3b
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.6666666667
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.3333333333

   Write the method ``isBalanced`` in the code below. The ``main`` method contains code to test your solution.
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
          ArrayList<String> delList = new ArrayList<String>();
   
          for (String currString : tokens)
          {
             if (currString.equals(openDel) || currString.equals(closeDel))
             {
                 delList.add(currString);
             }
          }
          return delList;
       }
   
       /** Returns true if the delimiters are balanced and false otherwise, as described in part (b).
        *  Precondition: delimiters contains only valid open and close delimiters.
        */
       public boolean isBalanced(ArrayList<String> delimiters)
       {
          /* to be implemented in part (b) */
       }
   
       public static void main(String[] args)
       {
           Delimiters d1 = new Delimiters("<sup>", "</sup>");
           String[] tokens = {"<sup>", "<sup>", "</sup>", "<sup>", "</sup>", "</sup>"};
           ArrayList<String> delList1 = d1.getDelimitersList(tokens);
           boolean res1 = d1.isBalanced(delList1);
           System.out.println("It should print true and it prints " + res1);
   
           String[] tokens2 = {"<sup>", "</sup>", "</sup>", "<sup>"};
           ArrayList<String> delList2 = d1.getDelimitersList(tokens2);
           boolean res2 = d1.isBalanced(delList2);
           System.out.println("It should print false and it prints " + res2);
   
           String[] tokens3 = {"</sup>"};
           ArrayList<String> delList3 = d1.getDelimitersList(tokens3);
           boolean res3 = d1.isBalanced(delList2);
           System.out.println("It should print false and it prints " + res3);
   
           String[] tokens4 = {"<sup>", "</sup>", "</sup>"};
           ArrayList<String> delList4 = d1.getDelimitersList(tokens4);
           boolean res4 = d1.isBalanced(delList2);
           System.out.println("It should print false and it prints " + res4);
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.util.*;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests()
        {
            super("Delimiters");
        }
   
        @Test
        public void test0()
        {
            String output = getMethodOutput("main");
            String expect = "It should print true and it prints true\nIt should print false and it prints false\nIt should print false and it prints false\nIt should print false and it prints false\n";
   
            boolean passed = getResults(expect, output, "Expected output from main: testing isBalanced on 4 sets of delimiters.");
            assertTrue(passed);
        }
   
        @Test
        public void test1()
        {
          Delimiters d1 = new Delimiters("{", "}");
   
          String[] tokens = {"{", "{", "}", "{", "}", "}"};
          ArrayList<String> delList1 = d1.getDelimitersList(tokens);
          boolean res1 = d1.isBalanced(delList1);
   
          boolean passed = getResults("true", ""+res1, "isBalanced works on a balanced set of delimiters "+ Arrays.toString(tokens));
   
          assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
          Delimiters d1 = new Delimiters("{", "}");
   
          String[] tokens2 = {"{", "}", "}", "{"};
          ArrayList<String> delList2 = d1.getDelimitersList(tokens2);
   
          boolean res2 = d1.isBalanced(delList2);
   
          boolean passed = getResults("false", ""+res2, "isBalanced on a non-balanced set of delimiters " +  Arrays.toString(tokens2));
   
          assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
          Delimiters d1 = new Delimiters("{", "}");
   
          String[] tokens3 = {"}"};
          ArrayList<String> delList3 = d1.getDelimitersList(tokens3);
   
          boolean res3 = d1.isBalanced(delList3);
   
          boolean passed = getResults("false", ""+res3, "isBalanced on a non-balanced set of delimiters " + Arrays.toString(tokens3));
   
          assertTrue(passed);
        }
   
        @Test
        public void test4()
        {
          Delimiters d1 = new Delimiters("{", "}");
   
          String[] tokens4 = {"{", "}", "}"};
          ArrayList<String> delList4 = d1.getDelimitersList(tokens4);
   
          boolean res4 = d1.isBalanced(delList4);
   
          boolean passed = getResults("false", ""+res4, "isBalanced on a non-balanced set of delimiters " + Arrays.toString(tokens4));
   
          assertTrue(passed);
        }
        }