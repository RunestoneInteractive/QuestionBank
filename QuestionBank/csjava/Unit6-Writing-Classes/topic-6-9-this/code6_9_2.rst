.. activecode:: code6_9_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csjava
   :chapter: Unit6-Writing-Classes
   :subchapter: topic-6-9-this
   :topics: Unit6-Writing-Classes/topic-6-9-this
   :from_source: T
   :language: java

   What does this code print out? Trace through the code. Notice how the this Pay object is passed to the Overtime constructor.
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