.. activecode:: hw_words_5000_pos_graph
    :author: Sean Joyce
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Files
    :subchapter: Exercises
    :topics: Files/Exercises
    :from_source: F

    In the first Chapter 10 project, you worked with a file of 
    the 5000 most common words in English.  (You may also wish
    to review that `project in the text <https://runestone.academy/runestone/books/published/fopp/Projects/common_words.html#common-words>`_
    for more info on the fields in that CSV file.)

    This exercise is the last exercise in that project. Using
    altair, let's look at the distribution of the different
    parts of speech in this 5000 word dataset.  Create a bar
    chart, where the part of speech is on the x-axis and
    the number of words on that list which fall into that
    category is on the y-axis.

    (Remember our `altair examples handout <https://drive.google.com/open?id=1RmdDm5awQ3nd79OD2fgzC5OcsyPrZBjLxhuibS0fOBI>`_.)
    
    If you want to check your work, your graph should look
    something like `this graph <https://drive.google.com/open?id=1tZhxhi_I_-CMmkB80NBoyx2dCgKa8cdAjda_YRtJ-oM>`_.

    ~~~~
    # we'll need altair for graphing
    import altair

    # leave this line as is, and work with the variable
    # it creates
    fileVar = open('words5000.csv', 'r')

    # your solution here

    fileVar.close()
    ====