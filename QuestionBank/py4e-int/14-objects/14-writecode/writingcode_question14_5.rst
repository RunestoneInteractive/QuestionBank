.. activecode:: writingcode_question14_5
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: 14-writecode
    :topics: 14-objects/14-writecode
    :from_source: T
    :nocodelens:

    class Book:

        def __init__(self, title, author):
            self.title = title
            self.author = author

    book = Book("The Odyssey", "Homer")
    print(book.getTitle())
    print(book.getTitle())