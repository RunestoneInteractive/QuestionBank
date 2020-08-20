.. activecode:: cturtle_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: Graphics
    :topics: Introduction/Graphics
    :from_source: T
    :language: cpp
    :optional:

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        //Create a turtle screen, and add our turtle to it.
        ct::TurtleScreen screen;
        ct::Turtle turtle(screen);

        //Set the turtle speed to the slowest available option.
        turtle.speed(ct::TS_SLOWEST);
        //Any number from 0 to 10 would work as well.
        //turtle.speed(7);

        //Sets the turtle's fill color to purple.
        turtle.fillcolor({"purple"});

        //Tells the turtle to begin filling a shape as it moves.
        turtle.begin_fill();

        //Tells the turtle to make a square.
        //Iterates once for every corner of the square.
        for (int i = 0; i < 4; i++) {

            //Tells the turtle to move forward 50 units.
            turtle.forward(50);

            //Tells the turtle to turn 90 degrees to the right.
            turtle.right(90);
        }

        //Tells the turtle to finish filling the shape it has outlined.
        turtle.end_fill();

        //Closes the turtle screen.
        screen.bye();
        return 0;
    }