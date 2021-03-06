.. activecode:: asu_cs_recursive_q1
    :author: Erdogan Dogdu
    :difficulty: 4.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5238095238
    :total_students_attempting: 21
    :num_students_correct: 17.0
    :mean_clicks_to_correct: 2.4705882353

    Write a **recursive** function ``reverseList(lst)`` that
    given a list ``lst``, returns a new list with the order of elements in ``lst``
    reversed. For example, list ``reverseList(['a','b','c'])`` should be
    return ``['c','b','a']``.
    
    Hint: Take the first element, reverse the remaining list and put the first element to the end of the new list and return.
    ~~~~
    def reverseList(lst):
        # Your recursive code here
    
    def main():
        # Your test code here
        print(reverseList(['a','b','c']))
    
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
    
            editText = self.getEditorText()
            self.assertEqual(0, len(re.findall("\s*while[( ]", editText)), "Should use no 'while' loops")
            self.assertEqual(0, len(re.findall("\s*for ", editText)), "Should use no 'for' loops")
    
            tests = [(['a','b','c'],['c','b','a']),
                 ([1], [1]),
                 ([], []),
                 ([1,2],[2,1])]
    
            for t in tests:
                self.assertEqual(reverseList(t[0]), t[1], 'Testing reverseList({}, {})'.format(t[0], t[1]) )
    
    myTests().main()