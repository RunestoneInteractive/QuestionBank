.. activecode:: tdq
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Dictionaries
    :subchapter: Aliasingandcopying
    :topics: Dictionaries/Aliasingandcopying
    :from_source: None

    opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
    alias = opposites

    print(alias is opposites)

    alias['right'] = 'left'
    print(opposites['right'])