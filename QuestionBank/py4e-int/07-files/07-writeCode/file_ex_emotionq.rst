.. activecode:: file_ex_emotionq
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 07-files
   :subchapter: 07-writeCode
   :topics: 07-files/07-writeCode
   :from_source: T
   :nocodelens:
   :available_files: emotion_words.txt

   Create a list called ``j_emotions`` that contains every word in ``emotion_words.txt``
   that begins with the letter "j".
   ~~~~


   =====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(j_emotions, ['joyous', 'jittery', 'jumpy'], "Testing that j_emotions was created correctly.")

   myTests().main()