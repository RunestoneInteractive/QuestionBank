.. parsonsprob:: 5_5_van_Mierlo
   :author: Matthijs van Mierlo
   :difficulty: 0.0
   :basecourse: apcsareview
   :chapter: Conditionals
   :subchapter: CondParsonsPractice
   :topics: Conditionals/CondParsonsPractice
   :from_source: F
   :numbered: left
   :adaptive:
   :noindent:

   The main method in the following class should print if your favorite food is junk food (pizza or wings) or not. But, the blocks have been mixed up and includes <b>an extra block</b> that is not needed in a correct solution.  Drag the needed blocks from the left and put them in the correct order on the right.  Click the <i>Check Me</i> button to check your solution.</p>
   -----
   public class Test1
   {
       public static void main(String[] args)
       {
   =====
           String favFood = "kale";
           boolean favPizza = favFood.equals("pizza");
           boolean favWings = favFood.equals("wings");
   =====
           if (favPizza || favWings)
           {
   =====
           if (favPizza && favWings) 
           { #paired
   =====
               System.out.println("You favorite food is junk food");
           }
   =====
           else
           {
   =====
               System.out.println("You favorite food is not junk food");
           }
   =====
       }
   }