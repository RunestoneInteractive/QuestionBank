.. activecode:: cturtle_practical_prompt
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: pattern_application
    :topics: Turtles/pattern_application
    :from_source: T
    :language: cpp

    #include <CTurtle.hpp>
    namespace ct = cturtle;

    int main() {
        ct::TurtleScreen scr;
        scr.tracer(0);//disable animation
        ct::Turtle turtle(scr);

        //Your code here

        scr.bye();
        return 0;
    }