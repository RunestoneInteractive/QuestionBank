.. activecode:: sdv
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: SimplePythonData
    :subchapter: Input
    :topics: SimplePythonData/Input
    :from_source: None

    str_seconds = input("Please enter the number of seconds you wish to convert")
    total_secs = int(str_seconds)

    hours = total_secs // 3600
    secs_still_remaining = total_secs % 3600
    minutes =  secs_still_remaining // 60
    secs_finally_remaining = secs_still_remaining  % 60

    print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)