.. mchoice:: vars_types_9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter2
    :subchapter: Exercises
    :topics: Chapter2/Exercises
    :from_source: T
    :pct_on_first: 0.25
    :total_students_attempting: 4
    :num_students_correct: 4.0
    :mean_clicks_to_correct: 3.25

    What line does the first error occur in the following program?
    If there is no error, what is the output?
    
    .. code-block::
       :linenos:
    
       int main() {
         char r = 'r';
         int x = 3;
         r = r + x;
         cout << r;
       }
    
    -   line 2, a variable cannot have the same name as its value
    
        -   A variable can have any value... as long as the types are
            the same.
    
    -   line 4, you cannot add an integer to a character
    
        -   Actually, C++ supports character operations!  This is legal.
    
    -   No error, ``rx``
    
        -   ``x`` is an integer, so what we really have is ``r = r + 3``.
    
    -   No error, ``r``
    
        -   ``'r'`` isn't necessarily the value of ``r``.  Take a look at line 4.
    
    -   No error, ``u``
    
        +   'u' is three letters after 'r', so on line 4, the value of ``u`` becomes
            the value of ``r``.