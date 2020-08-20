.. activecode:: dbj
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Debugging
    :subchapter: KnowyourerrorMessages
    :topics: Debugging/KnowyourerrorMessages
    :from_source: None

    str_time = input("What time is it now?")
    str_wait_time = input("What is the number of hours to wait?")
    time = int(str_time)
    wai_time = int(str_wait_time)

    time_when_alarm_go_off = time + wait_time
    print(time_when_alarm_go_off)