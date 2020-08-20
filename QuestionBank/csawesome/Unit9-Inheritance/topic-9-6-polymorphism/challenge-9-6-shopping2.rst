.. activecode:: challenge-9-6-shopping2
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit9-Inheritance
  :subchapter: topic-9-6-polymorphism
  :topics: Unit9-Inheritance/topic-9-6-polymorphism
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.0
  :total_students_attempting: 1
  :num_students_correct: 1.0
  :mean_clicks_to_correct: 2.0

  Copy in your code for DiscountedItem below and then write a method called countDiscountedItems which traverses the polymorphic ArrayLists of Items. Use instanceOf to test items to see if they are a DiscountedItem.
  ~~~~
  import java.util.*;
  
    /**
       The ShoppingCart class has an ArrayList of Items.
       You will write a new class DiscountedItem that extends Item.
       This code is adapted https://practiceit.cs.washington.edu/problem/view/bjp4/chapter9/e10-DiscountBill
    */
  
    public class Tester
    {
      public static void main(String[] args) {
        ShoppingCart cart = new ShoppingCart();
        cart.add(new Item("bread", 3.25));
        cart.add(new Item("milk", 2.50));
        //cart.add(new DiscountedItem("ice cream", 4.50, 1.50));
        //cart.add(new DiscountedItem("apples", 1.35, 0.25));
  
        cart.printOrder();
      }
    }
  
    class DiscountedItem extends Item
    {
        // Copy your code from the last lesson's challenge here!
    }
  
    // Add a method called countDiscountedItems()
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
  
                boolean passed = output.contains("ice cream") && output.contains("apples");
  
                getResults(expect, output, "Checking that DiscountedItem objects were added to ArrayList", passed);
                assertTrue(passed);
  
            }
  
            @Test
            public void test2()
            {
                String output = getMethodOutput("main");
                String expect = "Order Items:\n   bread $3.25\n   milk $2.50\n   ice cream $1.50 ($1.50)\n   apples $0.25 ($0.25)\nSub-total: $7.50\nDiscount: $1.75\nTotal: $5.75";
  
                boolean passed = !output.equals(expect);
  
                getResults(expect, output, "Checking that countDiscountedItems() was added to output", passed);
                assertTrue(passed);
  
            }
  
            @Test
            public void test3()
            {
                String output = getMethodOutput("main");
                String expect = "cart.countDiscountedItems()";
  
                boolean passed = checkCodeContains(expect);
                assertTrue(passed);
  
            }
  
            @Test
            public void test4()
            {
                String target = "public int countDiscountedItems()";
  
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
  
            }
  
            @Test
            public void test5()
            {
                String target = "if (* instanceof DiscountedItem)\n*++;";
  
                boolean passed = checkCodeContains(target);
                assertTrue(passed);
  
            }
        }