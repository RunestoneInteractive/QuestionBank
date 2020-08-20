.. activecode:: TurtleMethodsDistChallenge
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-5-methods-return
    :topics: Unit2-Using-Objects/topic-2-5-methods-return
    :from_source: F
    :language: java
    :datafile: turtleClassesReturn

    import java.util.*;
    import java.awt.*;
    import java.lang.Math;

    public class TurtleTestDistance
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);
          Turtle yertle = new Turtle(world);

          // Can you find yertle's distance from the point (0,0)?

          // Can you find the distance between 2 turtles?



          world.show(true);
      }
    }