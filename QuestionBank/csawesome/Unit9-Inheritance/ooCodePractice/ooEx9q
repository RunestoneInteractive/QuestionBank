.. activecode::  ooEx9q
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: ooCodePractice
   :topics: Unit9-Inheritance/ooCodePractice
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 2
   :num_students_correct: 2.0
   :mean_clicks_to_correct: 1.0

   Add public getter and setter methods to the Store class so its variables can be accessed by other classes.  It should print the store's name and address and then change both and print the new values.
   ~~~~
   public class Store
   {
       private String name;
       private String address;
   
       public Store(String theName, String theAddress)
       {
           this.name = theName;
           this.address = theAddress;
       }
   
       // ADD CODE HERE
   
       public String toString() { return this.name + "\n" + this.address; }
   
       public static void main(String[] args)
       {
           Store myStore = new Store("Barb's Store", "333 Main St.");
           System.out.println(myStore);
           myStore.setName("Barbara's Store");
           myStore.setAddress("555 Pine St.");
           System.out.println(myStore);
   
       }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;
    import java.io.*;
    import java.util.List;
    import java.util.ArrayList;
   
    public class RunestoneTests extends CodeTestHelper
    {
   
      @Test
      public void testMain() throws IOException
      {
        String output = getMethodOutput("main");
        String expect = "Barb's Store\n" +
                        "333 Main St.\n" +
                        "Barbara's Store\n" +
                        "555 Pine St.\n";
   
        boolean passed = getResults(expect, output, "Expected output from main");
        assertTrue(passed);
      }
   
      @Test
      public void test1()
      {
        Store myStore = new Store("A Store", "An Address");
   
        myStore.setName("Barbara's Store");
        myStore.setAddress("555 Pine St.");
   
        String output = myStore.getName() + "\n" + myStore.getAddress();
        String expect = "Barbara's Store\n" + "555 Pine St.";
   
        boolean passed = getResults(output, expect, "testing class Store: setters & getters");
        assertTrue(passed);
      }
    }