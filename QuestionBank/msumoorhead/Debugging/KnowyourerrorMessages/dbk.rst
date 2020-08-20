.. activecode:: dbk
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Debugging
    :subchapter: KnowyourerrorMessages
    :topics: Debugging/KnowyourerrorMessages
    :from_source: None

    n = input("What time is it now (in hours)?")
    n = imt(n)
    m = input("How many hours do you want to wait?")
    m = int(m)
    q = m % 12
    print("The time is now", q)