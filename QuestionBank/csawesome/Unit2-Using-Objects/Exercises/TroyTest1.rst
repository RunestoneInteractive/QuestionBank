.. activecode:: TroyTest1
    :author: Shawn Haarer
    :difficulty: 1.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: Exercises
    :topics: Unit2-Using-Objects/Exercises
    :from_source: F

    Try this  homework problem instead of an example in the text
    ~~~~
    import java.util.*;
    import java.awt.*;

    public class TurtleDraw8
    {
         public static void main(String[] args)
         {
              World world = new World(300,300);
              Turtle yertle = new Turtle(100, 200, world);
              // Make yertle draw an 8 with 2 squares
           
              yertle.forward();
              yertle.turnRight();
              yertle.forward();
              yertle.turnRight();

              world.show(true);
       }
       }