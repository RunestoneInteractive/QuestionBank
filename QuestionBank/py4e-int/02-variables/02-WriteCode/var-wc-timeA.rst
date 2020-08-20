.. activecode:: var-wc-timeA
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 02-variables
    :subchapter: 02-WriteCode
    :topics: 02-variables/02-WriteCode
    :from_source: T
    :optional:

    #prompt the user for the current time
    current_time_string = input("What is the current time (in hours)?")
    #prompt the user for the time to wait
    waiting_time_string = input("How many hours do you have to wait?")

    #convert the current time and the time to wait to integers
    current_time_int = int(current_time_string)
    waiting_time_int = int(waiting_time_string)

    #combine the two times
    hours = current_time_int + waiting_time_int

    #use the modulus operator to keep the time within 24 hours
    timeofday = hours % 24

    #print the time of day that the alarm will go off
    print(timeofday)