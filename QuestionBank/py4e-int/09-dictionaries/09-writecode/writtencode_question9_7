.. activecode:: writtencode_question9_7
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T

   phrase = "Exeggcute evolves into Exeggutor which are two extraordinary Pokemon"

   letter_count = {}
   for word in phrase.split():
       for letter in word:
           letter = letter.lower()
           if letter not in letter_count.keys():
               letter_count[letter] = 0
           letter_count[letter] += 1
   e_counter = letter_count['e']