.. parsonsprob:: mixedupcode_14_6
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: 14-mixedupcode
    :topics: 14-objects/14-mixedupcode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    Construct a class named "Book" that takes the title and author as initial values. Construct a class named "Bookinfo"
    that extends the "Book" class and contains a function "__str__" that  returns the string representation of the
    class.
    -----
    class Book:
    =====
     def __init__(self, title, author):
    =====
      self.title = title
      self.author = author
    =====
    class Bookinfo(Book):
    =====
     def __str__(self):
    =====
      return (self.title + " was written by " + self.author)
    =====
    iliad = Bookinfo("Iliad", "Homer")
    =====
    print(iliad)