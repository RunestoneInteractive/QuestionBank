.. activecode:: fileOpenInputa
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 07-files
    :subchapter: 07-userNames
    :topics: 07-files/07-userNames
    :from_source: T

    fname = input('Enter the file name: ') # Close parentheses
    fhand = open(fname) # Open the correct file name
    count = 0 # Start counting from zero
    for line in fhand:
        if line.startswith('Received:'):
        # Check at the beginning of the line, not the end
            count = count + 1 # Correct indentation.
    print('There were', count, 'lines starting with "Received:" in the file', fname)