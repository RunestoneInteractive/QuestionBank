.. parsonsprob:: ch5ex5muc
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit3-If-Statements
   :subchapter: topic-3-9-practice-mixed-code
   :topics: Unit3-If-Statements/topic-3-9-practice-mixed-code
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.6116708648
   :total_students_attempting: 2382
   :num_students_correct: 2258.0
   :mean_clicks_to_correct: 1.6899911426

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
   =====
           if (favPizza && favWings) #paired
   =====
               System.out.println("Your fav is junk food");
   =====
           else
   =====
               System.out.println("Your fav is not junk");
   =====
       }
   }