.. activecode:: answer10_8_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: T

    f = open('scarlet3.txt', 'r')
    contents = f.read()
    d = {}

    for w in contents.split():
        if len(w) == 7:
            if w not in d:
                d[w] = 1
            else:
                d[w] = d[w] + 1

    dkeys = d.keys()
    most_used = dkeys[0]
    for k in dkeys:
        if d[k] > d[most_used]:
            most_used = k

    print("The most used word is '"+most_used+"', which is used "+str(d[most_used])+" times")