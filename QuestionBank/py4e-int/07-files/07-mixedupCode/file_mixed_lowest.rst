.. parsonsprob:: file_mixed_lowest
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-mixedupCode
    :topics: 07-files/07-mixedupCode
    :from_source: T
    :numbered: left
    :adaptive:

    The following program prints the minimum PM 2.5 pollution found, but the code is mixed up.
    Drag the blocks of statements from the left column to the right column and put them in the
    right order. Watch your indentation.
    -----
    # read all the lines
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    # initialize the variables
    minCity = ''
    min25 = 500
    =====
    # loop through the lines
    for line in lines:
    =====
        # split at :
        values = line.split(":")
    =====
        # get the PM 2.5 pollution
        new25 = float(values[2])
    =====
        # if current <  min
        if new25 < min25:
    =====
            # save new min info
            minCity = values[0]
            min25 = new25
    =====
    # print the smallest PM 2.5 value
    print("Smallest PM 2.5 ",min25," in ",minCity)