.. parsonsprob:: file_mixed_largest
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-mixedupCode
    :topics: 07-files/07-mixedupCode
    :from_source: T
    :numbered: left
    :adaptive:

    PM 2.5 is an air pollutant that is harmful at high levels. The following program
    prints the maximum PM 2.5 pollution found, but the code is mixed up. Drag the blocks
    of statements from the left column to the right column and put them in the right order.
    Watch your indentation.
    -----
    # read all the lines
    inFile = open("uspoll.txt","r")
    lines = inFile.readlines()
    inFile.close()

    # initialize the variables
    maxCity = ''
    max25 = 0
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
        # if current > max
        if new25 > max25:
    =====
            # save the new max info
            maxCity = values[0]
            max25 = new25
    =====
    # print the largest PM 2.5 value
    print("Largest is ",max25," in ",maxCity)