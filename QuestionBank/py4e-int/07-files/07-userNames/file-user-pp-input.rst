.. parsonsprob:: file-user-pp-input
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-userNames
    :topics: 07-files/07-userNames
    :from_source: T
    :adaptive:
    :practice: T
    :numbered: left

    Put the following code in order to open and count the lines of a file from the user.
    Watch out for indentation and extra code blocks!
    -----
    fname = input('Enter the file name: ')
    =====
    fhand = open(fname)
    =====
    count = 0
    =====
    count = 1 #paired
    =====
    for line in fhand:
    =====
    for line in fname: #paired
    =====
        count = count + 1
    =====
    print('There were', count, 'lines in', fname)