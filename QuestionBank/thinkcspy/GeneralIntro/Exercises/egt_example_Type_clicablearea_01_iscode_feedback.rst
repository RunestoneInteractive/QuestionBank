.. clickablearea:: egt_example_Type_clicablearea_01_iscode_feedback
    :author: Eric Taucher (Instructor)
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: GeneralIntro
    :subchapter: Exercises
    :topics: GeneralIntro/Exercises
    :from_source: F
    :question: Click on all of the variables of type `int` in the code below
    :iscode: 
    :feedback: Remember input returns a `str`
    :pct_on_first: 0.2222222222
    :total_students_attempting: 9
    :num_students_correct: 8.0
    :mean_clicks_to_correct: 3.5

    :click-incorrect:seconds:endclick: = input("Please enter the number of seconds you wish to convert")
    
    :click-correct:hours:endclick: = int(seconds) // :click-incorrect:3600:endclick:
    :click-correct:secs_still_remaining:endclick: = :click-correct:total_secs:endclick: % 3600
    print(:click-correct:secs_still_remaining:endclick:)