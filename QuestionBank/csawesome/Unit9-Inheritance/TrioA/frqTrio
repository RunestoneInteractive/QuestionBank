.. activecode:: frqTrio
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit9-Inheritance
   :subchapter: TrioA
   :topics: Unit9-Inheritance/TrioA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 1
   :num_students_correct: 1.0
   :mean_clicks_to_correct: 1.0

   Write the Trio class (near the end of the code below) that implements the MenuItem interface (which is like extending a class). Your implementation must include a constructor that takes three parameters representing a sandwich, salad, and drink.  The main method has code to test the result.
   ~~~~
   import java.util.List;
   import java.util.ArrayList;
   import java.text.*;
   
   interface MenuItem
   {
      /** @return the name of the menu item */
      String getName();
   
      /** @return the price of the menu item */
      double getPrice();
   }
   
   class SimpleLunchItem implements MenuItem
   {
      private String name;
      private double price;
   
      public SimpleLunchItem(String aName, double aPrice)
      {
         name = aName;
         price = aPrice;
      }
   
      public String getName() { return name; }
      public double getPrice() { return price; }
   
      public String toString ()
      {
         DecimalFormat money = new DecimalFormat("0.00");
         return getName() + " " + money.format(getPrice());
      }
   }
   
   class Drink extends SimpleLunchItem
   {
      public Drink(String name, double price)
      { super(name, price); }
   }
   
   class Salad extends SimpleLunchItem
   {
      public Salad(String name, double price)
      { super(name, price); }
   }
   
   class Sandwich extends SimpleLunchItem
   {
      public Sandwich(String name, double price)
      { super(name, price); }
   }
   
   // Declare the Trio class.  It must implement the MenuItem interface.
   
   {
      // declare the fields that you need for a trio object
   
      // write a constructor that takes a Sandwich, Salad, and a Drink, in that order
   
      // write the getName method it should return
      // sandwich name/salad name/drink name Trio
   
      // write the getPrice method
      // it should return the price of the two highest price items in the trio.
   
      public static void main(String[] args)
      {
         Sandwich burger = new Sandwich("Cheeseburger",2.75);
         Sandwich club = new Sandwich("Club Sandwich", 2.75);
         Salad spinachSalad = new Salad("Spinach Salad",1.25);
         Salad coleslaw = new Salad("Coleslaw", 1.25);
         Drink orange = new Drink("Orange Soda", 1.25);
         Drink cap = new Drink("Cappuccino", 3.50);
         Trio trio1 = new Trio(burger,spinachSalad, orange);
         System.out.println("It should print Cheeseburger/Spinach Salad/Orange Soda Trio and it prints: " + trio1.getName());
         System.out.println("It should print 4.0 and it prints: " + trio1.getPrice());
         Trio trio2 = new Trio(club,coleslaw,cap);
         System.out.println("It should print Club Sandwich/Coleslaw/Capuccino Trio and it prints: " + trio2.getName());
         System.out.println("It should print 6.25 and it prints: " + trio2.getPrice());
      }
   }
   ====
   import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
   
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("Trio");
        }
   
        @Test
        public void test1()
        {
            String output = getMethodOutput("main");
            String expect = "It should print Cheeseburger/Spinach Salad/Orange Soda Trio and it prints: Cheeseburger/Spinach Salad/Orange Soda Trio\nIt should print 4.0 and it prints: 4.0\nIt should print Club Sandwich/Coleslaw/Capuccino Trio and it prints: Club Sandwi\nch/Coleslaw/Cappuccino Trio\nIt should print 6.25 and it prints: 6.25";
   
            boolean passed = removeSpaces(expect).equals(removeSpaces(output));
   
            getResults(expect, output, "Running main", passed);
            assertTrue(passed);
   
        }
   
        @Test
        public void test2()
        {
            String target = "implements MenuItem";
   
            boolean passed = checkCodeContains(target);
            assertTrue(passed);
        }
   
        @Test
        public void test3()
        {
            String output = checkConstructor("Sandwich, Salad, Drink");
            String expect = "pass";
   
            boolean passed = getResults(expect, output, "Checking Trio constructor with 3 arguments: Sandwich, Salad, Drink");
            assertTrue(passed);
        }
   
        @Test
        public void test4()
        {
            String target = "public String getName()";
   
            boolean passed = checkCodeContains("getName()", target);
            assertTrue(passed);
        }
   
        @Test
        public void test5()
        {
            String target = "public double getPrice()";
   
            boolean passed = checkCodeContains("getPrice()", target);
            assertTrue(passed);
        }
   
        @Test
        public void test6()
        {
            Sandwich burger = new Sandwich("Hamburger",7.50);
            Salad coleslaw = new Salad("Coleslaw", 2);
            Drink orange = new Drink("Orange Soda", 1.25);
            Trio trio1 = new Trio(burger, coleslaw, orange);
   
            String name = trio1.getName();
            String expect = "Hamburger/Coleslaw/Orange Soda Trio";
   
            boolean passed = getResults(expect, name, "Checking getName()");
            assertTrue(passed);
        }
   
        @Test
        public void test7()
        {
            Sandwich burger = new Sandwich("Hamburger",7.50);
            Salad coleslaw = new Salad("Coleslaw", 2);
            Drink orange = new Drink("Orange Soda", 1.25);
            Trio trio1 = new Trio(burger, coleslaw, orange);
   
            String name = "" + trio1.getPrice();
            String expect = "9.5";
   
            boolean passed = getResults(expect, name, "Checking getPrice()");
            assertTrue(passed);
        }
    }