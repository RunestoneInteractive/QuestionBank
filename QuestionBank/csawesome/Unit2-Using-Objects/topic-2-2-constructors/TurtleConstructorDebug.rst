.. activecode:: TurtleConstructorDebug
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-2-constructors
    :topics: Unit2-Using-Objects/topic-2-2-constructors
    :from_source: F
    :language: java
    :datafile: turtleClassesConstructor

    import java.util.*;
    import java.awt.*;

    public class TurtleConstructorDebug
    {
      public static void main(String[] args)
      {
          World w = new World(300,0);
          turtle t0;
          Turtle t1 = new Turtle();
          Turtle t2 = new Turtle(world, 100, 50)
          t0.forward();
          t1.turnRight();
          t2.turnLeft();
          world.show(true);
      }
    }