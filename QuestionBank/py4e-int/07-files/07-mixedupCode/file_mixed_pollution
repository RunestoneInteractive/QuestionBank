.. parsonsprob:: file_mixed_pollution
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-mixedupCode
    :topics: 07-files/07-mixedupCode
    :from_source: T
    :numbered: left
    :adaptive:

    The following program prints the pollution information for all cities that start with a ``D``,
    but the code is mixed up. Drag the blocks of statements from the left column to the right column
    and put them in the right order. Watch your indentation.
    -----
    # open the file for reading
    inFile = open("uspoll.txt","r")

    # read a line from the file
    line = inFile.readline()
    =====
    # while there is another line
    while line:
    =====
        # split at the :
        v = line.split(":")

        # get the city
        city = v[0]
    =====
        # if city starts with an D print info
        if (city.find("D") == 0):
            print('City: ', city)
            print("Pollution values:",v[1],v[2])
    =====
        # read the next line
        line = inFile.readline()
    =====
    # close the file
    inFile.close()