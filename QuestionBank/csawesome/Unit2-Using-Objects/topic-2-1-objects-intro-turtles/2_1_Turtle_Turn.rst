.. parsonsprob:: 2_1_Turtle_Turn
       :author: bmiller
       :difficulty: 3
       :basecourse: csawesome
       :topics: Unit2-Using-Objects/topic-2-1-objects-intro-turtles
       :from_source: T
       :numbered: left
       :adaptive: 
       :noindent: 
       :pct_on_first: 0.2422417786
       :total_students_attempting: 2159
       :num_students_correct: 2024.0
       :mean_clicks_to_correct: 3.6136363636

       The following program uses a turtle to draw the picture shown to the left, <img src="../_static/turtleTurnForwardRightForward.png" width="150" align="left" hspace="10" vspace="5" /> but the lines are mixed up.  The program should do all necessary set-up: import items, start the class definition, start the main method, and create a world and turtle. Then it should ask the turtle to turn 45 degrees, go forward 100 pixels, turn right, and then go forward 50 pixels. Next, it should ask the world to show itself. Finally, it should close the main method and class definition. We have added a compass to the picture to indicate the directions north, south, west, and east. <br /><br /><p>Drag the needed blocks of statements from the left column to the right column and put them in the right order.  There are <b>three extra blocks</b> that are not needed in a correct solution.  Then click on <i>Check Me</i> to see if you are right. You will be told if any of the lines are in the wrong order or are the wrong blocks.  </p>
       -----
       import java.util.*;
       import java.awt.*;
       =====
       public class TurtleTest {
       =====
           public static void main(String[] args) {
       =====
               World world = new World(300,300);
               Turtle yertle = new Turtle(world);
       =====
               yertle.turn(45);
       =====
               yertle.turnRight(45); #paired
       =====
               yertle.forward(100);
       =====
               yertle.turnRight();
       =====
               yertle.forward(50);
       =====
               yertle.forward(50; #paired
       =====
               world.show(true);
       =====
               world.show(true) #paired
       =====
           } // end main
       } // end class