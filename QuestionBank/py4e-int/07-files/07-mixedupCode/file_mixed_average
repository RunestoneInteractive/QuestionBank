.. parsonsprob:: file_mixed_average
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-mixedupCode
    :topics: 07-files/07-mixedupCode
    :from_source: T
    :numbered: left
    :adaptive:

    The following program prints the average PM 2.5 pollution found, but the code is
    mixed up. Drag the blocks of statements from the left column to the right column
    and put them in the right order. Watch your indentation.
    -----
    # read all the lines
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    # initialize the variables
    total25 = 0
    count = 1.0
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
        # add to the total and count
        total25 = total25 + new25
        count = count + 1
    =====
    # print the average PM 2.5 value
    print("Average PM 2.5 value is ",total25/count)