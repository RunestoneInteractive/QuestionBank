.. activecode:: writtencode_question14_9
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

      def getTitle(self):
          return self.title

      def getAuthor(self):
          return self.author

      def __repr__(self):
          return ( self.title + " was written by " + self.author)


   class Library:

     current_books = []

     def __init__(self, title, author):
         self.current_books.append(Book(title, author))

     def addBooks(self, title, author):
        self.current_books.append(Book(title, author))

     def __str__(self):
          return(str(self.current_books))



   newBook = Library("The Odyssey", "Homer")
   newBook.addBooks("Pride and Prejudice", "Jane Austen")
   print(newBook)