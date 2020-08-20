.. activecode:: cturtle_practical_example_cpp
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
        const int SQUARE_SIZE = 35;

        ct::TurtleScreen scr;
        scr.tracer(0);//disable animation
        ct::Turtle turtle(scr);
        turtle.speed(ct::TS_FASTEST);
        turtle.penup();

        for(int i = 0; i < 8; i++){
            turtle.goTo(-scr.window_width()/2,-scr.window_height()/2+ (i*SQUARE_SIZE)+SQUARE_SIZE);

            bool is_blue = i % 2 == 0;//even (true) or odd (false) row?

            for(int j = 0; j < 8; j++){
                ct::Color color;

                if(is_blue){
                    color = {"blue"};
                }else{
                    color = {"orange"};
                }

                turtle.begin_fill();
                turtle.fillcolor(color);

                for(int i = 0; i < 4; i++){
                    turtle.forward(SQUARE_SIZE);
                    turtle.right(90);
                }

                turtle.end_fill();

                turtle.forward(SQUARE_SIZE);
                is_blue = !is_blue;//flip-flop between true and false
            }
        }

        scr.bye();
        return 0;
    }