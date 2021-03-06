.. activecode:: asu_cs_dictionary_q3
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2916666667
    :total_students_attempting: 24
    :num_students_correct: 19.0
    :mean_clicks_to_correct: 3.3684210526

    Write a function ``count(lst1, lst2)`` that
    given lists ``lst1`` and ``lst2``, returns a dictionary
    with the elements of ``lst2`` as keys and the number of
    times each element of ``lst2`` occurring in ``lst1`` as the.        values. For example, ``count([0,1,2,3,4,1,2,3,2,3,5],[1,2,7])``
    returns ``{1: 2, 2: 3, 7: 0}``.
    
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
                self.assertEqual(count(t[0],t[1]), t[2], 'Testing count({},{}) -> {}'.format(t[0],t[1],t[2]) )
    
    myTests().main()