.. activecode:: 05section4_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 05-iterations
    :subchapter: 05-continue
    :topics: 05-iterations/05-continue
    :from_source: T
    :coach:
    :caption: A sample run of this new program with ``continue`` added.

    while True:
        line = raw_input('> ')
        if line[0] == '#' :
            continue
        if line == 'done':
            break
        else:
            print(line)
    print ('Done!')