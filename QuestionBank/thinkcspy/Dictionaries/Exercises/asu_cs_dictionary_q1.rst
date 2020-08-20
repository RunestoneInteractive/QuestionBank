.. activecode:: asu_cs_dictionary_q1
    :author: Erdogan Dogdu
    :difficulty: 5.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Write a function ``count(lst1, lst2)`` that
    given lists ``lst1`` and ``lst2``, returns a dictionary
    with the keys from ``lst2`` and the values as the number of

    ~~~~
    def count(lst1, lst2):
        # Your code here

    def main():
        # Your test code here
        print(count([0,1,2,3,4,1,2,3,2,3,5],[1,2,7]))

    if __name__ == "__main__":
        main()

    ====
    import re
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return

            print('Auto-testing...')

            tests = [(['a','b','c'],['a'],{'a':1}),
                 ([0,1,2,3,4,1,2,3,2,3,5],[1,2,7],{1: 2, 2: 3, 7: 0}),
                 ([1,1,1,2,2,3,0],[1,2,3],{1:3,2:2,3:1})]

            for t in tests:
                self.assertEqual(reverseList(t[0]), t[1], 'Testing reverseList({}, {})'.format(t[0], t[1]) )

    myTests().main()