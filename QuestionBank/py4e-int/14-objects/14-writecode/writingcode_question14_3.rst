.. activecode:: writingcode_question14_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: 14-writecode
    :topics: 14-objects/14-writecode
    :from_source: T
    :nocodelens:

    Class Book:

        title = ''
        author = ''

        def __init__(title, author):
            title = title
            author = author
            print("You book is " + title + " by author " + author)

    book = new Book("The Odyssey", "Homer")