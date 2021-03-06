.. mchoice:: vars_types_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter2
    :subchapter: Exercises
    :topics: Chapter2/Exercises
    :from_source: T
    :pct_on_first: 0.75
    :total_students_attempting: 4
    :num_students_correct: 4.0
    :mean_clicks_to_correct: 1.75

    What line does the first error occur in the following program?
    If there is no error, what is the output?
    
    .. code-block::
       :linenos:
    
       int main() {
         string Tom = "Tom";
         string friend = "Jerry";
         cout << tom;
         cout << "is friends with"; cout << friend;
       }
    
    -   line 2, a variable cannot have the same name as its value
    
        -   A variable can have any value... as long as the types are
            the same.
    
    -   line 3, you cannot have a variable named friend
    
        +   ``friend`` is a reserved keyword in C++ and can't be used
            as a variable name.  What a shame, since Tom and Jerry are
            the best of friends!
    
    -   line 5, you cannot have two statements on the same line
    
        -   You can have as many statements as you want on one line,
            as long as you terminate each one with a semicolon.
    
    -   No error, ``Tom is friends with Jerry``
    
        -   If the code runs, C++ doesn't automatically add spaces
            between consecutive strings.
    
    -   No error, ``Tomis friends withJerry``
    
        -   If the error was corrected, this would be the output.
            Unfortunately, there is an error that prevents this line
            from executing.