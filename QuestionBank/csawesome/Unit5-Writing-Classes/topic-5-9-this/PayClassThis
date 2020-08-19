.. activecode:: PayClassThis
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit5-Writing-Classes
   :subchapter: topic-5-9-this
   :topics: Unit5-Writing-Classes/topic-5-9-this
   :from_source: T
   :language: java
   :autograde: unittest
   :pct_on_first: 1.0
   :total_students_attempting: 118
   :num_students_correct: 118.0
   :mean_clicks_to_correct: 1.0

   What does this code print out? Trace through the code with the CodeLens button. Notice how the this Pay object is passed to the Overtime constructor.
   ~~~~
   public class Pay
   {
    private double pay;
   
    public Pay(double p)
    {
        pay = p;
    }
   
    public double getPay()
    {
        return pay;
    }
   
    public void calculatePayWithOvertime()
    {
        // this Pay object is passed to the Overtime constructor
        Overtime ot = new Overtime(this);
        pay = ot.getOvertimePay();
    }
   
    public static void main(String[] args)
    {
        Pay myPay = new Pay(100.0);
        myPay.calculatePayWithOvertime();
        System.out.println(myPay.getPay());
    }
   }
   
   class Overtime
   {
    private double payWithOvertime;
   
    public Overtime(Pay p)
    {
        payWithOvertime = p.getPay() * 1.5;
    }
   
    public double getOvertimePay()
    {
        return payWithOvertime;
    }
   }
   ====
    import static org.junit.Assert.*;
      import org.junit.*;
      import java.io.*;
   
      public class RunestoneTests extends CodeTestHelper
      {
            @Test
            public void testMain() throws IOException
            {
               String output = getMethodOutput("main");
                String expect = "150.0";
   
                boolean passed = getResults(expect, output, "Expected output from main", true);
                assertTrue(passed);
            }
      }