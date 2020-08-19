.. activecode:: code1_4_8
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit1-Getting-Started
   :subchapter: topic-1-4-assignment
   :topics: Unit1-Getting-Started/topic-1-4-assignment
   :from_source: T
   :language: java
   :autograde: unittest


   Complete the program based on the process shown in the Figure 3 flowchart.  Note the first line of code declares all 4 variables as type int.
   Add assignment statements and print statements to compute and print the slices per person and leftover slices.    Use System.out.println for output.
   ~~~~

    public class PizzaCalculator {

        public static void main(String[] args) {
            int pizzaSlices, numPeople, slicesPerPerson, leftoverSlices;
            //add your code

        }

    }

   ====
   import static org.junit.Assert.*;
   import org.junit.*;;
   import java.io.*;

   public class RunestoneTests extends CodeTestHelper
   {


    @Test
    public void test1()
    {
      String code = getCode();
      int count= countOccurences(code, "slicesPerPerson = pizzaSlices / numPeople;");
      boolean passed = (count== 1);

      passed = getResults("1 assignment slicesPerPerson", count+ " assignment slicesPerPerson", "compute slicesPerPerson", passed);
   }
    @Test
    public void test2()
    {
      String code = getCode();
      int count= countOccurences(code, "leftoverSlices = pizzaSlices % numPeople;");
      boolean passed = (count== 1);

      passed = getResults("1 assignment leftoverSlices", count+ " assignment leftoverSlices", "compute leftoverSlices", passed);
   }
   @Test
    public void test3()
    {
      String code = getCode();
      int count= countOccurences(code, "println(slicesPerPerson)");
      boolean passed = (count== 1);

      passed = getResults("1 print slicesPerPerson", count+ " print slicesPerPerson", "output slicesPerPerson", passed);
   }
   @Test
    public void test4()
    {
      String code = getCode();
      int count= countOccurences(code, "println(leftoverSlices)");
      boolean passed = (count== 1);

      passed = getResults("1 print leftoverSlices", count+ " print leftoverSlices", "output leftoverSlices", passed);
   }
   }