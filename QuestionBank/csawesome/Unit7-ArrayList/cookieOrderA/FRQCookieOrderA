.. activecode:: FRQCookieOrderA
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit7-ArrayList
   :subchapter: cookieOrderA
   :topics: Unit7-ArrayList/cookieOrderA
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 0.6666666667
   :total_students_attempting: 3
   :num_students_correct: 3.0
   :mean_clicks_to_correct: 1.3333333333

   FRQ Cookie Order Part A: Complete the method ``getTotalBoxes`` below.
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
      // Complete this method
    }
   
    public static void main(String[] args){
      boolean test1 = false;
      boolean test2 = false;
   
      MasterOrder order = new MasterOrder();
   
      if(order.getTotalBoxes() == 0)
        test1 = true;
      else
        System.out.println("Oops! Looks like your code doesn't properly check to see if the master order is empty.\n");
   
   
      order.addOrder(new CookieOrder("Raisin", 3));
      order.addOrder(new CookieOrder("Oatmeal", 8));
   
      if(order.getTotalBoxes() == 11)
        test2 = true;
      else
        System.out.println("Oops! Looks like your code doesn't properly count the number of boxes in the master order.\n");
   
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
            int total = order.getTotalBoxes();
   
            boolean passed = getResults("0", ""+total, "Empty order");
            assertTrue(passed);
        }
   
        @Test
        public void test2()
        {
            MasterOrder order = new MasterOrder();
            order.addOrder(new CookieOrder("Raisin", 4));
            order.addOrder(new CookieOrder("Oatmeal", 5));
   
            int total = order.getTotalBoxes();
   
            boolean passed = getResults("9", ""+total, "Test order of 4 boxes of Raisin and 5 Oatmeal");
            assertTrue(passed);
        }
    }