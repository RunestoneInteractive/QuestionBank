.. parsonsprob:: ch3ex4muc
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

   The main method in the following class should return the number of seconds in 5 days. But, the blocks have been mixed up and may include an extra block that isn't needed in the solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
   =====
       public static void main(String[] args)
       {
   =====
           int sInMin = 60;
           int mInHour = 60;
           int hInDay = 24;
   =====
           int sInDay = sInMin * mInHour * hInDay;
   =====
           int total = sInDay * 5;
   =====
           System.out.println(total);
   =====
       } // end main method
   =====
   } // end class
   =====
   public Class Test1
   { #distractor