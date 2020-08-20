.. parsonsprob:: question9_4_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-loopinganddictionaries
   :topics: 09-dictionaries/09-loopinganddictionaries
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Construct a block of code that adds the items in a dictionary to a list, where the items' values are greater than or equal to 8, and prints said list.
   -----
   books = {'Percy Jackson': 8, 'Harry Potter': 10, 'The Maze Runner': 10, 'The Hobbit': 7}
   =====
   list_o_books = []
   =====
   list_o_books = {} #distractor
   =====
   for title in books:
   =====
   for title in books #distractor
   =====
    if books[title] > 8: #distractor
   =====
    if books[title] ≥ 8:
   =====
     list_o_books.append(title)
   =====
   print(list_o_books)