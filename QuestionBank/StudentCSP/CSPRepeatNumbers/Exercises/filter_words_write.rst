.. activecode:: filter_words_write
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPRepeatNumbers
   :subchapter: Exercises
   :topics: CSPRepeatNumbers/Exercises
   :from_source: F
   :autograde: unittest
   :nocodelens: 
   :pct_on_first: 0.3376623377
   :total_students_attempting: 154
   :num_students_correct: 151.0
   :mean_clicks_to_correct: 3.8874172185

   Finish the function to return a new list with all the words removed that are of length 3 or less.  
   For example, (filter_words(["hi", "bye", "there"]) should return ["there"].  
   ~~~~
   def filter_words(word_list):
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
       def testOne(self):
           self.assertEqual(filter_words(["hi", "bye", "there"]), ["there"], 'filter_words(["hi", "bye", "there"])')
           self.assertEqual(filter_words(["hi", "bye"]), [], 'filter_words(["hi", "bye"])')
           self.assertEqual(filter_words(["I", "love", "you"]), ["love"], 'filter_words(["I", "love", "you"])')
           self.assertEqual(filter_words(["horse", "hour", "house"]), ["horse", "hour", "house"], 'filter_words(["horse", "hour", "house"])')
           self.assertEqual(filter_words(["love", "for", "all"]), ["love"], 'filter_words(["love", "for", "all"])')
    
   
   
              
   myTests().main()