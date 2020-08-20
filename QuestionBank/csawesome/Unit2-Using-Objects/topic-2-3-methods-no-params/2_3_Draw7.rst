.. parsonsprob:: 2_3_Draw7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-3-methods-no-params
   :topics: Unit2-Using-Objects/topic-2-3-methods-no-params
   :from_source: T
   :practice: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.5046826223
   :total_students_attempting: 1922
   :num_students_correct: 1843.0
   :mean_clicks_to_correct: 2.8209441129

   The following code uses a turtle to draw the digital number 7, but the lines are mixed up.  Drag the code blocks to the right and put them in the correct order to first draw the line going up (towards the top of the page) and then turn and draw a line to the left to make a 7. Remember that the turtle is facing the top of the page when it is first created. Click on the "Check Me" button to check your solution. </p>
   -----
   public class DrawL
   {
   =====
       public static void main(String[] args)
       {
   =====
           World habitat = new World(300,300);
   =====
           Turtle yertle = new Turtle(habitat);
   =====
           yertle.forward();
   =====
           yertle.turnLeft();
           yertle.forward();
   =====
           habitat.show(true);
   =====
       } // end main
   =====
   } // end class