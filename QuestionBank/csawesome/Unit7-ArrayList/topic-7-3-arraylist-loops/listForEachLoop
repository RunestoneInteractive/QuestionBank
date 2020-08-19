.. activecode:: listForEachLoop
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: topic-7-3-arraylist-loops
   :topics: Unit7-ArrayList/topic-7-3-arraylist-loops
   :from_source: T
   :language: java
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.380952381
   :total_students_attempting: 21
   :num_students_correct: 15.0
   :mean_clicks_to_correct: 1.5333333333

   What does the following code do? Guess before you run it. Then, add another enhanced for each loop that computes the product of all the elements in myList by multiplying them. Print out the product after the new loop.
   ~~~~
   import java.util.*;  // import all classes in this package.
   public class Test1
   {
       public static void main(String[] args)
       {
           ArrayList<Integer> myList = new ArrayList<Integer>();
           myList.add(50);
           myList.add(30);
           myList.add(20);
           int total = 0;
           for (Integer value: myList)
           {
                total += value;
           }
           System.out.println("Sum of all elements: " + total);
   
           // Write a for-each loop that computes the product
           // of all the elements in myList and print out the product.
   
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        @Test
        public void testExpected() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "100";
            boolean passed = output.contains(expect);
            getResults(expect, output, "Prints out sum", passed);
            assertTrue(passed);
        }
          @Test
        public void testProduct() throws IOException
        {
            String output = getMethodOutput("main");
            String expect = "30000";
            boolean passed = output.contains(expect);
            getResults(expect, output, "Prints out product", passed);
            assertTrue(passed);
        }
        @Test
        public void countForLoops()
        {
            String code = removeSpaces(getCode());
            int count = countOccurences(code,"for(Integer");
            boolean passed = count >= 2;
            getResults("2", count+"", "Number of for each loops", passed);
            assertTrue(passed);
        }
    }