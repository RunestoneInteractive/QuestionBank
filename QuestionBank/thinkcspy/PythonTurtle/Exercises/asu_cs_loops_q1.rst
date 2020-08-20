.. activecode:: asu_cs_loops_q1
    :author: Erdogan Dogdu
    :difficulty: 5.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python

    Write the function ``fibonacci_spiral(t, num)`` that, given a turtle object
    and a Fibonacci number (``num``), it will draw the Fibonacci spiral as
    explained here: https://en.wikipedia.org/wiki/Fibonacci_number.

    ~~~~
    def fibonacci_spiral(t, num):
        # write your code here
    
    
    # Test case
    import turtle
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.pensize(3)
    alex.color('red')

    fibonacci_spiral(alex, 5)

    wn.exitonclick()

    ====