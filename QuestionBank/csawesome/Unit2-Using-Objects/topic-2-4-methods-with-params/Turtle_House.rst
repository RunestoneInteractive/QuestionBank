.. activecode:: Turtle_House
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: csawesome
    :chapter: Unit2-Using-Objects
    :subchapter: topic-2-4-methods-with-params
    :topics: Unit2-Using-Objects/topic-2-4-methods-with-params
    :from_source: F
    :language: java
    :datafile: ModelDisplay.java, DigitalPicture.java, Pixel.java, SimplePicture.java, Turtle.java, SimpleTurtle.java, World.java, Picture.java, Pen.java, Giffer.java, PathSegment.java


    import java.util.*;
    import java.awt.*;

    public class TurtleHouse
    {
      public static void main(String[] args)
      {
          World world = new World(300,300);



          world.show(true);
      }
    }