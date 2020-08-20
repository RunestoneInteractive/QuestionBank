.. actex:: CS152_list_make_upper_comprehension
    :author: John Cigas
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Lists
    :subchapter: Exercises
    :topics: Lists/Exercises
    :from_source: F
    :practice: T
    :autograde: unittest
    :nocodelens:

    Write a fruitful function called ``make_upper(aList)`` that takes a list of strings as an argument
    and returns a list with all strings converted to upper case. Use a one line list comprehension.
    ~~~~

    def make_upper(aList):
        # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
         def testOne(self):
             l1 = ['ave', 'atque', 'vale']
             self.assertEqual(make_upper(l1),['AVE', 'ATQUE','VALE'],str(l1))
             l2 = ['Oh No!']
             self.assertEqual(make_upper(l2),['OH NO!'],str(l2))
             l3 = []
             self.assertEqual(make_upper(l3),[],str(l3))
             # Should check for empty list []



    myTests().main()