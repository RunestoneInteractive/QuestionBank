.. mchoice:: functions_mc3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter3
    :subchapter: Exercises
    :topics: Chapter3/Exercises
    :from_source: T
    :pct_on_first: 0.5
    :total_students_attempting: 2
    :num_students_correct: 2.0
    :mean_clicks_to_correct: 3.5

    **Multiple Response** Select all variables that have a *non-zero* value after the decimal place.
    (3.1 has a *non-zero* value, while 3.0 does not)
    
    ::
    
        #include <iostream>
        using namespace std;
    
        int main() {
          int a = 1.5;
          double b = a + 1.5;
          double c = 2.4;
          double d = 1/5;
          int e = c * c;
          double f = int(c);
        }
    
    -   ``a``
    
        -   C++ performs automatic type conversion to round 1.5 down to the
            nearest integer.
    
    -   ``b``
    
        +   Since ``a = 1``, we know that ``b = 2.5``, which is a non-zero decimal.
    
    -   ``c``
    
        +   ``c`` is a ``double`` and has a non-zero decimal.
    
    -   ``d``
    
        -   C++ performs integer division to round ``1/5`` down to the nearest
            integer.  The value will be stored as ``0``, not ``0.2``.
    
    -   ``e``
    
        -   ``c`` squared may have a non-zero decimal, but automatic type conversion
            will round it down to the nearest integer before storing the value in ``e``.
    
    -   ``f``
    
        -   ``int(c)`` rounds ``c`` down to the nearest integer before storing the
            value in ``f``.