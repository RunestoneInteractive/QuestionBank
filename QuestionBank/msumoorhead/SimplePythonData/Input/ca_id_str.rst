.. clickablearea:: ca_id_str
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: SimplePythonData
    :subchapter: Input
    :topics: SimplePythonData/Input
    :from_source: None
    :question: Click on all of the variables of type `str` in the code below
    :iscode:
    :feedback:

    :click-correct:seconds:endclick: = input(:click-incorrect:"Please enter the number of seconds you wish to convert":endclick:)

    :click-incorrect:hours:endclick: = int(:click-correct:seconds:endclick:) // :click-incorrect:3600:endclick:
    :click-incorrect:secs_still_remaining:endclick: = :click-incorrect:total_secs:endclick: % 3600
    print(:click-incorrect:secs_still_remaining:endclick:)