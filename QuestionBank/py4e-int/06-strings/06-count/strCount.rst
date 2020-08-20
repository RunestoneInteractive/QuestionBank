.. codelens:: strCount
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-count
    :topics: 06-strings/06-count
    :from_source: T
    :question: What is the value of count after the line with the red arrow executes?
    :breakline: 5
    :feedback: Use the variables box to look at the current value of count.
    :correct: globals.count

    word = 'raspberry'
    count = 0
    for letter in word:
        if letter == 'r':
            count = count + 1
    print(count)