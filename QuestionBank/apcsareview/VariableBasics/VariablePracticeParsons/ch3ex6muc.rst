.. parsonsprob:: ch3ex6muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: VariableBasics
   :subchapter: VariablePracticeParsons
   :topics: VariableBasics/VariablePracticeParsons
   :from_source: T
   :numbered: left
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
           double numGalls = miles / mpg;
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