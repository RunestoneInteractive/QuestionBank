.. activecode:: filerstrip
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-searching
    :topics: 07-files/07-searching
    :from_source: T
    :caption: Using rstrip with lines in a file
    :available_files: mbox-short3.txt

    fhand = open('mbox-short3.txt')
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:'):
            print(line)