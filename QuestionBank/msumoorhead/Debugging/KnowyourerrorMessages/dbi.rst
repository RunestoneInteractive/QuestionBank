.. activecode:: dbi
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Debugging
    :subchapter: KnowyourerrorMessages
    :topics: Debugging/KnowyourerrorMessages
    :from_source: None

    a = input('wpisz godzine')
    x = input('wpisz liczbe godzin')
    int(x)
    int(a)
    h = x // 24
    s = x % 24
    print (h, s)
    a = a + s
    print ('godzina teraz %s' %a)