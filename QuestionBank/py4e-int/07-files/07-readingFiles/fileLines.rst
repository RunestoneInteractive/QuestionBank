.. activecode:: fileLines
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-readingFiles
    :topics: 07-files/07-readingFiles
    :from_source: T
    :caption: Opening and counting the lines in a file
    :available_files: mbox-short2.txt

    fhand = open('mbox-short2.txt')
    count = 0
    for line in fhand:
        count = count + 1
    print('Line Count:', count)