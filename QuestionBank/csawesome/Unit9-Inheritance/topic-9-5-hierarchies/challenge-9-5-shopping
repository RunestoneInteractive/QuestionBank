.. activecode:: challenge-9-5-shopping
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-5-hierarchies
  :topics: Unit9-Inheritance/topic-9-5-hierarchies
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.2
  :total_students_attempting: 5
  :num_students_correct: 4.0
  :mean_clicks_to_correct: 2.0

  Complete the class DiscountedItem below that inherits from Item and adds an discount instance variable with a constructor, get/set, and a toString method. Uncomment the testing code in main to add discounted items to the cart.
  ~~~~
  import java.util.*;
  
    /**
       The ShoppingCart class has an ArrayList of Items.
       You will write a new class DiscountedItem that extends Item.
       This code is adapted from https://practiceit.cs.washington.edu/problem/view/bjp4/chapter9/e10-DiscountBill
    */
  
    public class Tester
    {
      public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        cart.add(new Item("bread", 3.25));
        cart.add(new Item("milk", 2.50));
  
        // Uncomment these to test
        //cart.add(new DiscountedItem("ice cream", 4.50, 1.50));
        //cart.add(new DiscountedItem("apples", 1.35, 0.25));
  
        cart.printOrder();
      }
    }
  
    // DiscountedItem inherits from Item
    class DiscountedItem extends Item
    {
        // add an instance variable for the discount
  
        // Add constructors that call the super constructor
  
        // Add get/set methods for discount
        public double getDiscount()
        {
          return 0.0; // return discount here instead of 0
        }
  
        // Add a toString() method that returns a call to the super toString
        // and then the discount in parentheses using the super.valueToString() method
  
    }
  
    class ShoppingCart
    {
        private ArrayList<Item> order;
        private double total;
        private double internalDiscount;
  
        public ShoppingCart()
        {
            order = new ArrayList<Item>();
            total = 0.0;
            internalDiscount = 0.0;
        }
  
        public void add(Item i) {
            order.add(i);
            total += i.getPrice();
            if (i instanceof DiscountedItem)
               internalDiscount += ((DiscountedItem) i).getDiscount();
        }
  
       /** printOrder() will call toString() to print */
        public void printOrder() {
            System.out.println(this);
        }
  
        public String toString() {
            return discountToString();
        }
  
        public String discountToString() {
            return orderToString() + "\nSub-total: " + valueToString(total) + "\nDiscount: " + valueToString(internalDiscount) + "\nTotal: " + valueToString(total - internalDiscount);
        }
  
        private String valueToString(double value) {
            value = Math.rint(value * 100) / 100.0;
            String result = "" + Math.abs(value);
            if(result.indexOf(".") == result.length() - 2) {
                result += "0";
            }
            result = "$" + result;
            return result;
        }
  
        public String orderToString() {
            String build = "\nOrder Items:\n";
            for(int i = 0; i < order.size(); i++) {
                build += "   " + order.get(i);
                if(i != order.size() - 1) {
                    build += "\n";
                }
            }
            return build;
        }
      }
  
      class Item {
        private String name;
        private double price;
  
        public Item()
        {
          this.name = "";
          this.price = 0.0;
        }
  
        public Item(String name, double price) {
                this.name = name;
                this.price = price;
        }
  
        public double getPrice() {
                return price;
        }
  
        public String valueToString(double value) {
                String result = "" + Math.abs(value);
                if(result.indexOf(".") == result.length() - 2) {
                    result += "0";
                }
                result = "$" + result;
                return result;
        }
  
        public String toString() {
                return name + " " + valueToString(price);
        }
       }
       ====
       import static org.junit.Assert.*;
        import org.junit.*;;
        import java.io.*;
  
        public class RunestoneTests extends CodeTestHelper
        {
            public RunestoneTests() {
                super("Tester");
            }
  
            @Test
            public void test1()
            {
                String output = getMethodOutput("main");
                String expect = "Order Items:\n   bread $3.25\n   milk $2.50\n   ice cream $1.50 ($1.50)\n   apples $0.25 ($0.25)\nSub-total: $7.50\nDiscount: $1.75\nTotal: $5.75";
  
                boolean passed = getResults(expect, output, "Running main", true);
                assertTrue(passed);
  
            }
  
            @Test
            public void test2()
            {
                String output = getMethodOutput("main");
                String expect = "Order Items:\n   bread $3.25\n   milk $2.50\n   ice cream $1.50 ($1.50)\n   apples $0.25 ($0.25)\nSub-total: $7.50\nDiscount: $1.75\nTotal: $5.75";
  
                boolean passed = output.contains("ice cream") && output.contains("apples");
  
                getResults(expect, output, "Checking that DiscountedItem objects were added to ArrayList", passed);
                assertTrue(passed);
  
            }
  
            @Test
            public void test3()
            {
                String target = "String, double, double";
  
                boolean passed = getResults("pass", checkConstructor(target), "Checking constructor with arguments: " + target);
                assertTrue(passed);
  
            }
  
            @Test
            public void test4()
            {
                String target = "public double getDiscount()";
  
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
  
            }
  
            @Test
            public void test5()
            {
                String target = "public String toString()";
  
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
  
            }
  
            @Test
            public void test6()
            {
                String target = "super.toString()";
  
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
  
            }
  
            @Test
            public void test7()
            {
                String target = "super.valueToString(*)";
  
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
  
            }
        }