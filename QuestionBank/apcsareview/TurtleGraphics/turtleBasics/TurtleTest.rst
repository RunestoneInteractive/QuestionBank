.. activecode:: TurtleTest
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: TurtleGraphics
    :subchapter: turtleBasics
    :topics: TurtleGraphics/turtleBasics
    :from_source: T
    :language: java
    :datafile: turtleClasses

    import java.util.*;

    public class TurtleTest
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);
          Turtle myrtle = new Turtle(world);

          yertle.forward(100);
          yertle.turnLeft();
          yertle.forward(75);

          myrtle.turnRight();
          myrtle.forward(100);

          world.show(true);
      }
    }