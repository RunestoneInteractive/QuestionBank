.. mchoice:: mce_7_8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter7
    :subchapter: Exercises
    :topics: Chapter7/Exercises
    :from_source: T
    :practice: T

    What is the output of the code below?

    .. code-block:: cpp

     int main() {
       string tongue_twister = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?";
       int index = find (quote, 'w', quote.find("wood") + 1);
       cout << index;
     }

    - 9

      - Take a closer look at the starting index for where we should start looking.

    - 22

      + After the first 'w', the second 'w' appears at index 22.

    - 43

      - Take a closer look at the ``find`` function and its arguments.

    - 65

      - Take a closer look at the ``find`` function and its arguments.