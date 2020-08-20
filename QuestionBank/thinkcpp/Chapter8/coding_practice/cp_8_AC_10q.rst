.. activecode:: cp_8_AC_10q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: coding_practice
    :topics: Chapter8/coding_practice
    :from_source: T
    :language: cpp
    :stdin: 145, 2
    :practice: T

    Ever wanted to know how much you'd weigh on each planet? Write the ``convertWeight``
    function, which takes a ``double earthWeight`` and ``int planet`` as parameters. First,
    in ``main``, prompt the user to enter their weight in pounds and a number corresponding to
    a planet (Mercury is 1, Venus is 2, etc.). Next, call the ``convertWeight`` function using
    the user's input. Finally, print out their weight on that planet.
    If the user inputs an invalid planet, print out an error message.
    The weight conversion are as follows (multiply the number by ``earthWeight`` to get the weight on that planet):
    Mercury - 0.38, Venus - 0.91, Earth - 1.00, Mars - 0.38, Jupiter - 2.34, Saturn - 1.06, Uranus - 0.92, and Neptune - 1.19.
    Below are some examples.

    ::

        Please enter your weight in pounds: 145.6
        Please select a planet: 3
        Your weight on Earth is 145.6 pounds.

        or

        Please enter your weight in pounds: 170
        Please select a planet: 1
        Your weight on Mercury is 64.6 pounds.

        or

        Please enter your weight in pounds: 170
        Please select a planet: 23
        Error, not a valid planet.
    ~~~~
    #include <iostream>
    using namespace std;

    double convertWeight (double earthWeight, int planet) {
        // Write your implementation here.
    }

    int main() {
        // Write your implementation here.
    }