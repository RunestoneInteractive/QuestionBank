.. mchoice:: double_to_int_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcpp
    :chapter: Chapter3
    :subchapter: ConvertingFromDoubleToInt
    :topics: Chapter3/ConvertingFromDoubleToInt
    :from_source: T
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 4.0

    Your final grade consists of your average performance on exam 1 and exam 2.
    Your professor is using C++ to grade the exams and allows you to choose which
    method you'd like your exam to be graded.
    
    ::
    
          double exam1 = 88.8;
          double exam2 = 72.7;
          double exam2 = 97.9;
    
    **Method 1:**
    
    ::
    
          double final = (int(exam1) + int(exam2) + int(exam3)) / 3;
    
    **Method 2:**
    
    ::
    
          int final = int((exam1 + exam2 + exam3) / 3);
    
    Which method would you choose and why?
    
    -   **Method 1:** ``final`` is a ``double``, meaning my final grade will
        have more digits past the decimal, and will be higher than the ``int``
        in Method 2.
    
        -   Although ``final`` is a ``double``, it doesn't have any digits past
            the decimal due to the integer division.
    
    -   **Method 1:** the rounding happens at the beginning, so all three of my
        test scores will be rounded to the nearest ``int``, which in my case, will
        round all of them up.
    
        -   Converting to an ``int`` always rounds *down*, even if your ``double`` is very
            close to the next integer.
    
    -   **Method 2:** ``final`` is an ``int``, so it gets rounded up.
    
        -   Converting to an ``int`` always rounds *down*, even if your ``double`` is very
            close to the next integer.
    
    -   **Method 2:** the rounding happens at the very end, so my grade will be higher!
    
        +   Always save your rounding until the end!