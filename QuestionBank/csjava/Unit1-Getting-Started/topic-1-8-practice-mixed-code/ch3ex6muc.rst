.. parsonsprob:: ch3ex6muc
   :author: bmiller
   :difficulty: 3
   :basecourse: csjava
   :topics: Unit1-Getting-Started/topic-1-8-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:
   :noindent:

   The main method in the following class should calculate the cost of a trip that is 200 miles when the price of gas is 2.20 and the miles per gallon is 42. But, the blocks have been mixed up and may include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
   =====
       {
   =====
           int miles = 200;
           double price = 2.20;
           int mpg = 42;
   =====
           double numGalls = (double) miles / mpg;
   =====
           double totalCost = numGalls * price;
   =====
           System.out.println(totalCost);
   =====
       }
   =====
   }
   =====
           System.println(totalCost); #distractor