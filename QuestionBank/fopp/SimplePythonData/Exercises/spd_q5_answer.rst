.. activecode:: spd_q5_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: T
    :nocanvas:

    ## question 5 solution ##

    current_time_string = input("What is the current time (in hours)? ")
    waiting_time_string = input("How many hours do you have to wait? ")

    current_time_int = int(current_time_string)
    waiting_time_int = int(waiting_time_string)

    hours = current_time_int + waiting_time_int

    timeofday = hours % 24

    print(timeofday)