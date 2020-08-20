.. activecode:: codeexample1
   :author: Brad Miller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: _sources
   :subchapter: index
   :topics: _sources/index
   :from_source: F
   :coach:
   :caption: This is a caption

   print("My first program adds a list of numbers")
   myList = [2, 4, 6, 8, 10]
   total = 0
   for num in myList:
       total = total + num
   print(total)