.. activecode:: fileFrom
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-searching
    :topics: 07-files/07-searching
    :from_source: T
    :caption: Printing lines starting with "From:"
    :available_files: mbox-short3.txt

    fhand = open('mbox-short3.txt')
    count = 0
    for line in fhand:
        if line.startswith('From:'):
            print(line)