.. activecode:: Turtle_Names4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: StudentCSP
    :chapter: CSPNameTurtles
    :subchapter: changeProg
    :topics: CSPNameTurtles/changeProg
    :from_source: T
    :tour_1: "Line-by-line Tour"; 1: first-turtle-line-1; 2: first-turtle-line-2; 3: first-turtle-line-3; 4: first-turtle-line-4; 5: first-turtle-line-5; 6: first-turtle-line-6;
    :nocodelens:

    from turtle import *        # use the turtle library
    space = Screen()            # create a turtle screen (space)
    alex = Turtle()             # create a turtle named alex
    alex.forward(150)           # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
    alex.forward(75)            # tell alex to move forward by 75 units