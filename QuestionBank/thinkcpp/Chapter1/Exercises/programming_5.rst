.. mchoice:: programming_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter1
    :subchapter: Exercises
    :topics: Chapter1/Exercises
    :from_source: T
    :pct_on_first: 0.2
    :total_students_attempting: 5
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 2.6

    What type of error would the following code cause?  Assume you are
    trying to calculate the volume of a cylinder:
    
    ::
    
        int radius = 7;
        int height = 8;
        double volume = 3.14 * radius * height;
    
    -   syntax error
    
        -   There is nothing wrong with the structure of this program.
    
    -   run-time error
    
        -   There are no errors that will surface at runtime.
    
    -   semantic error
    
        +   This is not the correct formula for calculating the volume of a
            cylinder.  This program will go on to calculate the wrong volume
            because it doesn't know any better.
    
    -   no error
    
        -   Take a look at the area formula.