.. activecode:: sks_cw7_ex1
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    The greatest common divisior GCD of two integers ``a`` and ``b`` is the largest
    integer ``k`` that divides both ``a`` and ``b`` evenly. (That is, ``k`` divides both
    ``a`` and ``b`` without leaving a remainder.)

    For example, ``gcd( 6, 9 ) == 3`` because 3 evenly divides both 6 and 9 and
    no greater integer does so. Another example, ``gcd( 25, 55 ) == 5``.

    Here is a math-like definition of GCD:

    .. sourcecode:: python

        gcd(0, n) = n

        gcd(a, b) = gcd( b % a, a )  % is the remainder after integer division b/a

    For example.

    .. sourcecode:: python

        gcd( 6, 9 ) = gcd( 9 % 6, 6 ) = gcd( 3, 6 )
        gcd( 3, 6 ) = gcd( 6 % 3, 3 ) = gcd( 0, 3 )
        gcd( 0, 3 ) = 3 

    Translate the math-like definition of gcd into a recursive Python function.
    Write a main() function to test it.     
    ~~~~
    def gcd(a, b):
        # Your recursive code here

    def main():
        # Your test code here
    
    if __name__ == "__main__":
        main()
    ====