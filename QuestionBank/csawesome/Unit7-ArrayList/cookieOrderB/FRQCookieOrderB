.. activecode:: FRQCookieOrderB
  :author: bmiller
  :difficulty: 3.0
  :basecourse: csawesome
  :chapter: Unit7-ArrayList
  :subchapter: cookieOrderB
  :topics: Unit7-ArrayList/cookieOrderB
  :from_source: T
  :language: java
  :autograde: unittest
  :pct_on_first: 0.5
  :total_students_attempting: 2
  :num_students_correct: 2.0
  :mean_clicks_to_correct: 2.0

  FRQ Cookie Order B: Complete the method ``removeVariety`` below.
  ~~~~
  import java.util.List;
  import java.util.ArrayList;
  
  class CookieOrder
  {
   private int numBoxes;
   private String variety;
  
   /** Constructs a new CookieOrder object */
   public CookieOrder(String variety, int numBoxes)
   {
     this.variety = variety;
     this.numBoxes = numBoxes;
   }
  
   /** @return the variety of cookie being ordered
   */
   public String getVariety()
   { return this.variety; }
  
   /** @return the number of boxes being ordered
   */
   public int getNumBoxes()
   { return this.numBoxes; }
  
   // There may be instance variables, constructors, and methods that are not shown.
  }
  
  public class MasterOrder
  {
   /** The list of all cookie orders */
   private List<CookieOrder> orders;
  
   /** Constructs a new MasterOrder object */
   public MasterOrder()
   { orders = new ArrayList<CookieOrder>(); }
  
   /** Adds theOrder to the master order.
   *   @param theOrder the cookie order to add to the master order
   */
   public void addOrder(CookieOrder theOrder)
   { orders.add(theOrder); }
  
   /** @return the sum of the number of boxes of all of the cookie orders
   */
   public int getTotalBoxes(){
     int sum = 0;
      for (CookieOrder co : this.orders) {
        sum += co.getNumBoxes();
      }
      return sum;
   }
  
   public int removeVariety(String cookieVar){
    // Complete this method
   }
  
   public static void main(String[] args){
     boolean test1 = false;
     boolean test2 = false;
  
     MasterOrder order = new MasterOrder();
     order.addOrder(new CookieOrder("Raisin", 3));
     order.addOrder(new CookieOrder("Oatmeal", 8));
     order.addOrder(new CookieOrder("Sugar", 2));
  
     if(order.removeVariety("Raisin") == 3 && order.removeVariety("Sugar") == 2)
       test1 = true;
     else
       System.out.println("Oops! Looks like your code doesn't return the correct value for cookie order varieties that exist.\n");
  
     if(order.removeVariety("Chocolate Chip") == 0)
       test2 = true;
     else
       System.out.println("Oops! Looks like your code doesn't return the correct value for cookie orders that don't exist in the master order.\n");
  
     if(test1 && test2)
       System.out.println("Looks like your code works well!");
     else
       System.out.println("Make some changes to your code, please.");
   }
  }
  ====
  import static org.junit.Assert.*;
    import org.junit.*;;
    import java.io.*;
  
    public class RunestoneTests extends CodeTestHelper
    {
        public RunestoneTests() {
            super("MasterOrder");
        }
  
        @Test
        public void test0() {
            String output = getMethodOutput("main");
            String expected = "Looks like your code works well!";
  
            boolean passed = getResults(expected, output, "main()");
            assertTrue(passed);
        }
  
        @Test
        public void test1()
        {
            MasterOrder order = new MasterOrder();
            order.addOrder(new CookieOrder("Raisin", 3));
            order.addOrder(new CookieOrder("Oatmeal", 8));
            order.addOrder(new CookieOrder("Raisin", 4));
            order.addOrder(new CookieOrder("Oatmeal", 8));
  
            int total = order.removeVariety("Raisin");
  
            boolean passed = getResults("7", ""+total, "Remove variety with 7 boxes");
            assertTrue(passed);
        }
  
        @Test
        public void test2()
        {
            MasterOrder order = new MasterOrder();
            order.addOrder(new CookieOrder("Raisin", 3));
            order.addOrder(new CookieOrder("Oatmeal", 8));
            order.addOrder(new CookieOrder("Raisin", 4));
            order.addOrder(new CookieOrder("Oatmeal", 8));
  
            int total = order.removeVariety("Chocolate Chip");
  
            boolean passed = getResults("0", ""+total, "Remove order with 0 boxes");
        }
    }