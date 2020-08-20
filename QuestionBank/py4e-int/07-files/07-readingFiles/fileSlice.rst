.. activecode:: fileSlice
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-readingFiles
    :topics: 07-files/07-readingFiles
    :from_source: T
    :caption: Using the read function with files
    :available_files: mbox-short2.txt

    fhand = open('mbox-short2.txt')
    inp = fhand.read()
    print(len(inp))
    print(inp[:20])