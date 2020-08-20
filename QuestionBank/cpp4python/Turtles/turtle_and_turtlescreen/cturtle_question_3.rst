.. parsonsprob:: cturtle_question_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: Turtles
    :subchapter: turtle_and_turtlescreen
    :topics: Turtles/turtle_and_turtlescreen
    :from_source: T

    Construct a program that fills a green triangle using begin_fill and end_fill
    using the example code above as a guide.
    -----
    #include <CTurtle.hpp>
    namespace ct = cturtle;
    =====
    int main(){
    =====
        ct::TurtleScreen scr;
        ct::Turtle turtle(scr);
    =====
        turtle.fillcolor({"green"});
    =====
        turtle.begin_fill();
    =====
        for(int i = 0; i < 3; i++){
            turtle.forward(50);
            turtle.right(60);
        }
    =====
        turtle.end_fill();
    =====
        scr.bye();
    =====
        return 0;
    =====
    }