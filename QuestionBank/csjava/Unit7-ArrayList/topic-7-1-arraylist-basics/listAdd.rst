.. activecode:: listAdd
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit7-ArrayList/topic-7-1-arraylist-basics
   :from_source: T
   :language: java
   :autograde: unittest

   Can you add another item to the shopping list?
   ~~~~
   import java.util.*;
   public class Shopping
   {
      public static void main(String[] args)
      {
         ArrayList<String> shoppingList = new ArrayList<String>();
         System.out.println("Size: " + shoppingList.size());
         shoppingList.add("carrots");
         System.out.println(shoppingList);
         shoppingList.add("bread");
         System.out.println(shoppingList);
         shoppingList.add("chocolate");
         System.out.println(shoppingList);
         System.out.println("Size: " + shoppingList.size());
         ArrayList<Integer> quantities = new ArrayList<Integer>();
         quantities.add(2);
         quantities.add(4);
         System.out.println(quantities);
     }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;

    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Shopping");
        }

        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "Size: 0\n[carrots]\n[carrots, bread]\n[carrots, bread, chocolate]\nSize: 3\n[2, 4]";

            boolean passed = !output.equals(expect);

            passed = getResults(expect, output, "Changes to main()", passed);
            assertTrue(passed);
        }

    }