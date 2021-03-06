.. mchoice:: mce_6_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter6
    :subchapter: Exercises
    :topics: Chapter6/Exercises
    :from_source: T
    :practice: T

    Why are we allowed to use the variable ``x`` in both ``main`` and in the function definition of ``superSecretFunction``?

    .. code-block:: cpp

     int superSecretFunction (int n) {
       int x = 0;
       return (2 + (n * n) - 5 * n / 7) * x;
     }

     int main() {
       int x = 1;
       cout << "After using the super secret function, we get " << superSecretFunction (x);
     }

    - We're using the same variable, but just reassigning the value from 0 to 1.

      - We are actually using two different variables that happen to have the same name.

    - Although the name of both variables is ``x``, they represent different locations in memory, and thus are different variables.

      + One ``x`` is a local variable of ``superSecretFunction`` while the other is a local variable of ``main``.

    - We can assign them different values but not the same value. Thus, if both were initialized to 0, then we'd get an error.

      - Since they are not in the same storage location, they can store any value, including the same value.

    - We're not allowed to do this. The code will result in an error.

      - The code does not produce an error.