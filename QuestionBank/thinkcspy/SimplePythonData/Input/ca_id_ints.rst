.. clickablearea:: ca_id_ints
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Input
    :topics: SimplePythonData/Input
    :from_source: T
    :question: Click on all of the variables of type `int` in the code below
    :iscode: 
    :feedback: Remember input returns a `str`
    :pct_on_first: 0.0412147505
    :total_students_attempting: 21206
    :num_students_correct: 19070.0
    :mean_clicks_to_correct: 4.5171997902

    :click-incorrect:seconds:endclick: = input("Please enter the number of seconds you wish to convert")
    
    :click-correct:hours:endclick: = int(:click-incorrect:seconds:endclick:) // 3600
    :click-correct:total_secs:endclick: = int(:click-incorrect:seconds:endclick:)
    :click-correct:secs_still_remaining:endclick: = :click-correct:total_secs:endclick: % 3600
    print(:click-correct:secs_still_remaining:endclick:)