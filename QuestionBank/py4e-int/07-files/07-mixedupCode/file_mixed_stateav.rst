.. parsonsprob:: file_mixed_stateav
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-mixedupCode
    :topics: 07-files/07-mixedupCode
    :from_source: T
    :numbered: left
    :adaptive:

    The following program prints the average PM 2.5 pollution for a state, but the code is
    mixed up. Drag the blocks of statements from the left column to the right column and put
    them in the right order. Watch your indentation.
    -----
    # read all the lines
    infile = open("uspoll.txt","r")
    lines = infile.readlines()
    infile.close()

    # initialize the variables
    state = "CA"
    total25 = 0
    count = 1.0
    =====
    # loop through the lines
    for line in lines:
    =====
        # split at :
        values = line.split(":")
    =====
        # split at ,
        cityState = values[0].split(",")
    =====
        # if found state
        if cityState[1].find(state) >= 0:
    =====
            # add the current to the sum
            new25 = float(values[2])
            total25 = total25 + new25

            # increment the count
            count = count + 1
    =====
    # print the average
    avg = total25/count
    print("Avg for " , state, " is ", avg)