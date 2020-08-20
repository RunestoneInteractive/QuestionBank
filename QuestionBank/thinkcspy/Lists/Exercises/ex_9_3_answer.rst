.. activecode:: ex_9_3_answer
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: T

   myList = [76, 92.3, 'hello', True, 4, 76]

   myList.append("apple")         # a
   myList.append(76)              # a
   myList.insert(3, "cat")        # b
   myList.insert(0, 99)           # c

   print(myList.index("hello"))   # d
   print(myList.count(76))        # e
   myList.remove(76)              # f
   myList.pop(myList.index(True)) # g

   print (myList)