.. activecode:: fileFind
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-searching
    :topics: 07-files/07-searching
    :from_source: T
    :caption: Finding and printing specific lines from a file
    :available_files: mbox-short3.txt

    fhand = open('mbox-short3.txt')
    for line in fhand:
        line = line.rstrip()
        if line.find('@uct.ac.za') == -1:
            continue
        print(line)