.. parsonsprob:: mixedupcode_14_9
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

    Construct a class named "Book" that contains title, author and format as initial values. Create a class named
    "Library" that extends "Book" and has available as initial value, a function named updateAvailability to update
    availability and a function named "__str__" that returns the string representation of the class.
    -----
    class Book:
    =====
     def __init__(self, title, author, format):
    =====
        self.tite = title
        self.author = author
        self.format = format
    =====
    class Library(Book):
    =====
     def __init__(Book(title, author, format), available): #distractor
    =====
     def __init__(self, title, author, format, available):
    =====
      self.book = Book(title, author, format) #distractor
    =====
      Book.__init__(title, author, format)
    =====
       self.format = format
       self.available = available
    =====
     def updateAvailability(self, available)
    =====
       self.available = available
    =====
     def __str__(self):
    =====
       return ("Author: " + self.author + " Title: " + self.title + " Format: " + self.format + "Available: " + self.available)
    =====
    iliad = Library("Iliad", "Homer", "Paperback" , "Yes")
    =====
    iliad.updateAvailability("No")
    print(iliad)