.. activecode:: cturtle_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: introduction
    :topics: Turtles/introduction
    :from_source: T
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);
        turtle.speed(ct::TS_SLOWEST);
        turtle.fillcolor({"purple"});
        turtle.begin_fill();
        for (int i = 0; i < 4; i++) {
            turtle.forward(50);
            turtle.right(90);
        }
        turtle.end_fill();
        scr.bye();
        return 0;
    }