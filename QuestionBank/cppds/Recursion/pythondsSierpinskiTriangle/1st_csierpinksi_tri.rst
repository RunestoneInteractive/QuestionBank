.. activecode:: 1st_csierpinksi_tri
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Recursion
    :subchapter: pythondsSierpinskiTriangle
    :topics: Recursion/pythondsSierpinskiTriangle
    :from_source: T
    :caption: Drawing a Sierpinski Triangle
    :language: cpp

    #include <CTurtle.hpp>

    namespace ct = cturtle;

    void draw_triangle(ct::Point a, ct::Point b, ct::Point c, ct::Color color, ct::Turtle& myTurtle){
        myTurtle.fillcolor(color);
        myTurtle.penup();
        myTurtle.goTo(a);
        myTurtle.pendown();
        myTurtle.begin_fill();
        myTurtle.goTo(c);
        myTurtle.goTo(b);
        myTurtle.goTo(a);
        myTurtle.end_fill();
    }

    //getMid already defined as "middle" function in C-Turtle namespace :)

    void sierpinski(ct::Point a, ct::Point b, ct::Point c, int degree, ct::Turtle& myTurtle){
        const std::string colormap[] = {"blue", "red", "green", "white", "yellow", "violet", "orange"};
        draw_triangle(a,b,c, {colormap[degree]}, myTurtle);
        if(degree > 0){
            sierpinski(a, ct::middle(a, b), ct::middle(a, c), degree - 1, myTurtle);
            sierpinski(b, ct::middle(a, b), ct::middle(b, c), degree - 1, myTurtle);
            sierpinski(c, ct::middle(c, b), ct::middle(a, c), degree - 1, myTurtle);
        }
    }

    int main() {
        ct::TurtleScreen screen;
        screen.tracer(3);//Draw faster.
        ct::Turtle turtle(screen);

        ct::Point myPoints[] = {
            {-100, -50},
            {0, 100},
            {100, -50}
        };

        sierpinski(myPoints[0], myPoints[1], myPoints[2], 3, turtle);

        screen.bye();
        return 0;
    }