.. activecode:: listParsing
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-parsing
    :topics: 08-lists/08-parsing
    :from_source: T
    :caption: Parsing a file using lists and split.
    :available_files: mboxShort.txt

    fhand = open('mboxShort.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        print(words[2])

    # Continue is used here to skip the rest of the line if it doesn't start with "From "