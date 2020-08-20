.. activecode:: ex1
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Exceptions
    :subchapter: 01_intro_exceptions
    :topics: Exceptions/01_intro_exceptions
    :from_source: None

    h = int(input('enter the hour'))
    if h < 1 or h > 12:
        raise Exception
    print('valid hour')