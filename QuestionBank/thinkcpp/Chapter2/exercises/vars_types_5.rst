.. mchoice:: vars_types_5
    :author: bmiller
    :difficulty: 3
    :basecourse: thinkcpp
    :topics: Chapter2/exercises
    :from_source: T

    **Multiple Response** What could be changed so that the output of
    the following program is ``34``?

    .. code-block::
       :linenos:

       int main() {
         char c;
         int d;
         c = "3";
         d = 4;
         cout << c; cout << d;
       }

    -   ``c`` should be declared as an int.

        -   This will still result in an error.

    -   ``c`` should be declared as a string.

        +   This clears up the type mismatch on line 4.

    -   ``d`` should be declared as a char.

        -   Although the code will still run, it won't give correct output.

    -   Line 4 should be replaced with ``c = 3``

        -   Although the code will still run, it won't give correct output.

    -   Line 4 should be replaced with ``c = '3'``

        +   This clears up the type mismatch on line 4.