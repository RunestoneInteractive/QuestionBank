.. parsonsprob:: mixedupcode_question9_10
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-mixedupcode
   :topics: 09-dictionaries/09-mixedupcode
   :from_source: T
   :numbered: left
   :practice: T
   :adaptive:

   Place the code in the correct order so it properly counts the amount of characters in a sentence using the .get() method.
   -----
   sentence = "The quick brown fox jumped over the lazy dog"
   =====
   characters = {}
   =====
   characters = dictioanry #distractor
   =====
   for character in sentence:
   =====
   for character in sentence.split(): #distractor
   =====
    characters[character] = characters.get(character, 0) + 1
   =====
    characters[character] = characters.get(character, 1) #distractor
   =====
   print(characters)