.. activecode:: cp_8_AC_6q
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter8
    :subchapter: coding_practice
    :topics: Chapter8/coding_practice
    :from_source: T
    :language: cpp
    :practice: T

    Write the ``Pokemon`` structure, which has instance variables ``string pokeName``,
    ``string type``, ``int level``, and ``int healthPercentage`` in that order.
    Next, write the function ``printPokeInfo``, which takes a ``Pokemon`` as a parameter and outputs the
    Pokemon's info in the following format: ``pokeName`` (Lv. ``level``, ``healthPercentage``\% HP).
    ~~~~
    #include <iostream>
    using namespace std;

    struct Pokemon {
        // Write your implementation here.
    };

    void printPokeInfo (Pokemon p) {
        // Write your implementation here.
    }

    int main() {
        Pokemon magikarp = { "Magikarp", "Water", 12, 100 };
        printTrainerInfo (magikarp);
    }