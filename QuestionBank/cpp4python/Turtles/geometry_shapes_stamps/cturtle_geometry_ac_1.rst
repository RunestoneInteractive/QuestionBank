.. activecode:: cturtle_geometry_ac_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: geometry_shapes_stamps
    :topics: Turtles/geometry_shapes_stamps
    :from_source: T
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main(){
        ct::TurtleScreen screen;
        screen.tracer(1, 1000);
        ct::Turtle turtle(screen);

        ct::Polygon upside_down_triangle = {
          {0, 0},   //First point
          {-5, -5}, //Second point
          {5, -5}  //and so on.
        };

        turtle.shape(upside_down_triangle);
        turtle.forward(50);

        screen.bye();
        return 0;
    }