.. activecode:: csw_exp_2
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :autograde: unittest
   :language: python3

   Write a function to add names and phone numbers, one name and number
   at a time, to a dictionary. Send the dictionary, the name, and the 
   number to the function. Remember that dictionaries are mutable so 
   it's not necessary to return anything.
   ~~~~
   def add_name(phone_book, name, number):
      #Add your code here

   phone_dict = {}
   add_name(phone_dict, "Jay", "555-1234")
   add_name(phone_dict, "Jan", "555-5678")
   ====
   from unittest import TestCase

   class myTests(TestCase):

     def testOne(self):
         self.assertEqual(phone_dict["Jan"],"555-5678","Tested phone_dict on string 'Jan'")

   myTests().testOne()