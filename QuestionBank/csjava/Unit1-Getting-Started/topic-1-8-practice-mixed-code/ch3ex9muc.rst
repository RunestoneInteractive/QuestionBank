.. parsonsprob:: ch3ex9muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit1-Getting-Started/topic-1-8-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The main method in the following class should calculate how much you will have to pay for an item that is 60% off the original price of $52.99. But, the blocks have been mixed up and may include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
   =====
       {
   =====
           double price = 52.99;
           double discount = 0.6;
   =====
           double savings = price * discount;
   =====
           double finalPrice = price - savings;
   =====
           System.out.println(finalPrice);
   =====
       }
   =====
   }
   =====
          int price = 52.99;
          int discount = 0.6; #distractor