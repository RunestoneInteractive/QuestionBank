.. clickablearea:: ca_id_ints
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: SimplePythonData
    :subchapter: Input
    :topics: SimplePythonData/Input
    :from_source: None
    :question: Click on all of the variables of type `int` in the code below
    :iscode:
    :feedback: Remember input returns a `str`

    :click-incorrect:seconds:endclick: = input("Please enter the number of seconds you wish to convert")

    :click-correct:hours:endclick: = int(seconds) // :click-incorrect:3600:endclick:
    :click-correct:secs_still_remaining:endclick: = :click-correct:total_secs:endclick: % 3600
    print(:click-correct:secs_still_remaining:endclick:)