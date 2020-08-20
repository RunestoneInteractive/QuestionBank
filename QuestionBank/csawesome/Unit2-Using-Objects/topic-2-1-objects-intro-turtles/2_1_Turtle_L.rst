.. parsonsprob:: 2_1_Turtle_L
   :author: bmiller
   :difficulty: 3.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: topic-2-1-objects-intro-turtles
   :topics: Unit2-Using-Objects/topic-2-1-objects-intro-turtles
   :from_source: T
   :practice: T
   :numbered: left
   :adaptive: 
   :noindent: 
   :pct_on_first: 0.2286044719
   :total_students_attempting: 2594
   :num_students_correct: 2398.0
   :mean_clicks_to_correct: 5.4841534612

   The following program uses a turtle to draw a sort-of sideways capital L as shown to the left, <img src="../_static/turtleForwardLeftForward.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import items, start the class definition, start the main method, and create a habitat and turtle. Then it should ask the turtle to turn right, go forward, turn left, and then go forward 50 pixels. Next, it should ask the habitat to show itself.  Finally, it should close the main method and class definition. We have added a compass to the picture to indicate the directions north, south, west, and east. <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order.  There are <b>three extra blocks</b> that are not needed in a correct solution.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.  </p>
   -----
   import java.util.*;
   import java.awt.*;
   =====
   public class TurtleTest {
   =====
       public static void main(String[] args) {
   =====
           World habitat = new World(300,300);
           Turtle yertle = new Turtle(habitat);
   =====
           yertle.turnRight();
   =====
           yertle.right(); #paired
   =====
           yertle.forward();
   =====
           yertle.forward() #paired
   =====
           yertle.turnLeft();
   =====
           yertle.forward(50);
   =====
           habitat.show(true);
   =====
           habitat.show(True); #paired
   =====
       } // end main
   } // end class