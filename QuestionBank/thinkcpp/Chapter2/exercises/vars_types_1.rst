.. mchoice:: vars_types_1
    :author: bmiller
    :difficulty: 3
    :basecourse: thinkcpp
    :topics: Chapter2/exercises
    :from_source: T

    Take a look at the following program.  How many lines of output will be produced?

    ::

        int main() {
          int hour = 7;
          int min = 50;
          cout << "The current time is: " << endl;
          cout << hour;
          cout << ":";  cout << minute;
          cout << endl;
          cout << "I'm going to be late for my 8am!";
        }

    -   6

        -   There *are* 6 ``cout`` statements, but that doesn't mean there are 6 lines of output!

    -   5

        -   There *are* 5 lines of ``cout`` statments, but that doesn't mean there are 5 lines of output!

    -   3

        +   Even though there are 6 ``cout`` staments written on 5 lines, there are only 3 lines
            of output in the terminal.

    -   2

        -   There *are* 2 ``endl`` statements.  But what happens when you have more output after
            the ``endl``?

    -   0! There is an error!

        -   Everything is syntacticly legal! You can have ``cout`` statements on *multiple lines of code*
            that have *one* line of output... or you can have multiple ``cout`` statements on *one* line of
            code that have *multiple* lines of output!