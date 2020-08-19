.. activecode:: code3_2_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-2-ifs
   :topics: Unit3-If-Statements/topic-3-2-ifs
   :from_source: T
   :language: java
   :stdin: 16 0
   :autograde: unittest

   Update the program based on the conditional control flow shown in Figure 2.  Add an if statement to test the value stored in numPeople.
   Don't forget curly braces around the 4 lines for computing and printing slicesPerPerson and leftoverSlices.

   Run the program multiple times with negative, 0, and positive values for number of people.  The program should no longer result in a divide by zero exception.
   ~~~~
    import java.util.Scanner;
    public class PizzaCalculatorInput {

        public static void main(String[] args) {
            int pizzaSlices, numPeople, slicesPerPerson, leftoverSlices;
            Scanner scan = new Scanner(System.in);
            pizzaSlices = scan.nextInt();
            numPeople = scan.nextInt();

            slicesPerPerson = pizzaSlices / numPeople;
            leftoverSlices = pizzaSlices % numPeople;
            System.out.println(slicesPerPerson);
            System.out.println(leftoverSlices);

        }

    }
   ====
    import static org.junit.Assert.*;
    import org.junit.After;
    import org.junit.Before;
    import org.junit.Test;

    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {

    @Test
    public void test1a()
    {
      String code = getCode();
      int count= countOccurences(code, "if (numPeople > 0)");
      boolean passed = (count== 1);

      passed = getResults("1 numPeople > 0", count+ " numPeople > 0", "Missing test: if (numPeople > 0)", passed);
    }
    }