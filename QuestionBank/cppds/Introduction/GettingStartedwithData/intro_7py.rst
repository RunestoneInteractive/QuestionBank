.. activecode:: intro_7py
    :author: Brad Miller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: F
    :caption: Using a Dictionary

    capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
    print(capitals['Iowa'])
    capitals['Utah']='SaltLakeCity'
    capitals['California']='Sacramento'
    print(len(capitals))
    for k in capitals:
        print(capitals[k]," is the capital of ", k)