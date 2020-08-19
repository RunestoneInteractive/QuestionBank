.. activecode:: writingcode_question9_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :practice: T
   :nocodelens:

   Write a program to read through a mail log, build a histogram using the dictionary "user_count" to count how many messages have come from each email address, and print the dictionary.
   ~~~~

   mail_log = ['From stephen.marquard@uct.ac.za Sat Jan  7', 'From gopal.ramasammycook@gmail.com Thurs Jan  5', 'From stephen.marquard@uct.ac.za Sat Feb  7', 'From louis@media.berkeley.edu Tues Jan  3', 'From stephen.marquard@uct.ac.za Sat Nov  6', 'From antranig@caret.cam.ac.uk Sat Jan  7', 'From david.horwitz@uct.ac.za Wed Jan  4', 'From ray@media.berkeley.edu Mon Jan  2', 'From stephen.marquard@uct.ac.za Mon Jan 2', 'From wagnermr@iupui.edu Fri Jan  6', 'From gopal.ramasammycook@gmail.com Thurs Dec  5', 'From louis@media.berkeley.edu Tues April  1']

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
         def testOne(self):
             self.assertEqual(len(user_count), 7, "Making sure the amount of messages sent is correct.")
             self.assertEqual(user_count['stephen.marquard@uct.ac.za'], 4, "Checking that this email address is counted for 4 times.")

   myTests().main()