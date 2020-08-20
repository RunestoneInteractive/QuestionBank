.. activecode:: uniqueid
   :author: Shawn Haarer
   :difficulty: 1.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: Exercises
   :topics: Unit2-Using-Objects/Exercises
   :from_source: F

   :language: java
   

    If this is a homework problem instead of an example in the text
    then the assignment text should go here.  The assignment text ends with
    the line containing four tilde ~
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleDraw8
    {
  public static void main(String[] args)
      {
      World world = new World(300,300);
      Turtle yertle = new Turtle(world);
      // Make yertle draw an 8 with 2 squares
      yertle.forward();
      yertle.turnRight();
      yertle.forward();

      world.show(true);
      }
    }