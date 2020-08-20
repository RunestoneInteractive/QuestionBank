.. activecode:: tdp
   :author: jenkins
   :difficulty: 3.0
   :basecourse: msumoorhead
   :chapter: Dictionaries
   :subchapter: Dictionarymethods
   :topics: Dictionaries/Dictionarymethods
   :from_source: None

   inventory = {'bananas': 312, 'oranges': 525, 'pears': 217, 'apples': 430}


   for akey in inventory.keys():
       print("key:", akey, "value:", inventory[akey])