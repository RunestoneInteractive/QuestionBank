.. clickablearea:: egt_example_Type_clicablearea_02_iscode_feedback
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
    :pct_on_first: 0.2
    :total_students_attempting: 10
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 3.4

    :click-incorrect:seconds:endclick: = input(:click-incorrect:"Please enter the number of seconds you wish to convert":endclick:)
    
    :click-correct:hours:endclick: :click-incorrect:=:endclick: :click-incorrect:int:endclick:(:click-incorrect:seconds:endclick:) // :click-incorrect:3600:endclick:
    :click-correct:secs_still_remaining:endclick: :click-incorrect:=:endclick: :click-correct:total_secs:endclick: :click-incorrect:%:endclick: :click-incorrect:3600:endclick:
    :click-incorrect:print:endclick:(:click-correct:secs_still_remaining:endclick:)