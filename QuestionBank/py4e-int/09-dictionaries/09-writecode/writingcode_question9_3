.. activecode:: writingcode_question9_3
   :author: bmiller
   :difficulty: 3.0
   :basecourse: py4e-int
   :chapter: 09-dictionaries
   :subchapter: 09-writecode
   :topics: 09-dictionaries/09-writecode
   :from_source: T
   :practice: T
   :nocodelens:

   mail = ['From stephen.marquard@uct.ac.za Sat Jan  7', 'From gopal.ramasammycook@gmail.com Thurs Jan  5', 'From louis@media.berkeley.edu Tues Jan  3', 'From antranig@caret.cam.ac.uk Sat Jan  7', 'From david.horwitz@uct.ac.za Wed Jan  4', 'From ray@media.berkeley.edu Mon Jan  2', 'From stephen.marquard@uct.ac.za Mon Jan 2', 'From wagnermr@iupui.edu Fri Jan  6']

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(mail_count['Mon'], 2, "Making sure only two emails are associated with Monday.")
           self.assertEqual(mail_count['Sat'], 2, "Checking that there are 2 emails sent on Saturday.")
           self.assertEqual(mail_count.get('Sun', 0), 0, "Checking that no emails were sent on Sunday.")

   myTests().main()