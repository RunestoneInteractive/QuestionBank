.. mchoice:: vars_types_10
    :author: bmiller
    :difficulty: 3
    :basecourse: thinkcpp
    :topics: Chapter2/exercises
    :from_source: T

    Suppose you want to find the volume of a cone.  For reference,
    the formula is ``V = 1/3 pi * r^2 * h``.  For the sake of this
    question, we will use ``pi = 3.14``.  What is wrong with the
    following code?

    ::

       double volume(r, h) {
         return 1/3 * 3.14 * r * r * h;
       }

    -   semantic error

        +   With integer division, ``1 / 3`` becomes 0.  Multiplying 0
            by the rest of the expression will always return 0, which is
            not what you want your program to do!

    -   syntax error

        -   There is nothing wrong with the structure of your program.

    -   run-time error

        -   There are no errors that will surface at run-time.

    -   You can't calculate and return on the same line!

        -   You actually can, this is called composition.

    -   Nothing!  There is not an error.

        -   This formula will return a volume, but is it correct?