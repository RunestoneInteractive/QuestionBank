.. activecode:: turtle_checkyourself_ac_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: check_yourself
    :topics: Turtles/check_yourself
    :from_source: T
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);

        turtle.begin_fill();

        for(int i = 0; i < 4; i++){
            turtle.forward(50);
            turtle.right(90);
        }

        turtle.end_fill();

        scr.bye();
        return 0;
    }