.. activecode:: act_code_hu_file_words5000_10
    :author: Sean Joyce
    :difficulty: 4.0
    :basecourse: fopp
    :chapter: Files
    :subchapter: Exercises
    :topics: Files/Exercises
    :from_source: F

    In the first Chapter 10 project, you worked with a file of the 5000 most common words in English.  (You may wish to review the `project in the the text <https://runestone.academy/runestone/static/heidelberg_ac101s19/Files/common_words.html>`_ for more info on the fields in that CSV file.)   This exercise is the last exercise in that project.  Using altair, let's look at the distribution of the different parts of speech in this 5000 word dataset.  Create a bar chart, where the part of speech is on the x-axis and the number of words on that list that fall into that category is on the y-axis. (Remember our `altair examples <https://drive.google.com/open?id=1B468Awg8ythCwSFeqRHfv8qOxove6CVzGdcUO3Gtkio>`_ handout.)

    ~~~~
    # we'll need altair for graphing
    import altair

    # open the file for reading
    fileVar = open("words5000.csv", "r")

    # your solution here