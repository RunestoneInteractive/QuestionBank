.. activecode:: intro_7
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Introduction
    :subchapter: GettingStartedwithData
    :topics: Introduction/GettingStartedwithData
    :from_source: T
    :caption: Using a Dictionary

    capitals = {"Iowa": "Des Moines", "Wisconsin": "Madison"}
    print(capitals["Iowa"])
    capitals["Utah"] = "Salt Lake City"
    print(capitals)
    capitals["California"] = "Sacramento"
    print(len(capitals))
    for k in capitals:
        print(capitals[k],"is the capital of", k)