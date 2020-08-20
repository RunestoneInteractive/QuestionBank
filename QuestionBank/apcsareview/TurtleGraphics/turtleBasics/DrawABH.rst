.. parsonsprob:: DrawABH
   :author: bmiller
   :difficulty: 3.0
   :basecourse: apcsareview
   :chapter: TurtleGraphics
   :subchapter: turtleBasics
   :topics: TurtleGraphics/turtleBasics
   :from_source: T
   :numbered: left
   :adaptive:
   :noindent:

   The following code uses a turtle to draw a capital A, but the lines are mixed up.  Drag the code blocks to the right and put them in the correct order to draw the A in the order shown by the numbers in the picture above.  Click on the "Check Me" button to check your solution. It may help to act out the code pretending you are the turtle. Remember that the angles you turn depend on which direction you are facing, and the turtle begins facing up. You can also try this code in the Java program above to see what the turtle will do.
   -----
   public class TurtleDrawA
   {
   =====
      public static void main(String[] args)
      {
      =====
         World world = new World(300,300);
         =====
         Turtle yertle = new Turtle(world);
         =====
         yertle.turn(15);
         yertle.forward(100);
         =====
         yertle.turnRight();
         yertle.turn(55);
         yertle.forward(100);
         =====
         yertle.penUp();
         yertle.backward(50);
         yertle.penDown();
         =====
         yertle.turnRight();
         yertle.turn(20);
         yertle.forward(30);
         =====
         world.show(true);
         =====
      }
      =====
   }