.. activecode:: answer10_8_2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F

    pirate = {}
    pirate['sir'] = 'matey'
    pirate['hotel'] = 'fleabag inn'
    pirate['student'] = 'swabbie'
    pirate['boy'] = 'matey'
    pirate['restaurant'] = 'galley'
    #and so on

    sentence = input("Please enter a sentence in English")

    psentence = []
    words = sentence.split()
    for aword in words:
        if aword in pirate:
            psentence.append(pirate[aword])
        else:
            psentence.append(aword)

    print(" ".join(psentence))