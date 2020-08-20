.. activecode:: asu_cs_rec_q1
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: IntroRecursion
    :subchapter: Exercises
    :topics: IntroRecursion/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.3076923077
    :total_students_attempting: 13
    :num_students_correct: 6.0
    :mean_clicks_to_correct: 2.0

    Write a **recursive** function ``sum(lst)`` that
    ``lst`` is a list of numbers, and the function returns
    the sum of these numbers.
    
    ~~~~
    def sum(lst):
        # Your code here
    
    def main():
        # Your test code here
        print(sum([3,4,1,5,6,7]))
    
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
    
            code = self.getEditorText()
            self.assertEqual(self.getEditorText().count('sum('), 3, 'Make sure you have recursive call')
    
            tests = [
                 ([0,1,2,3],6,'sum({})->{}'),
                 ([1,3,5,-4,7,-1],11,'sum({})->{}'),
                 ([0],0,'sum({})->{}'),
                 ([],0,'sum({})->{}')]
    
            for t in tests:
                self.assertEqual(sum(t[0]), t[1], t[2].format(t[0],t[1]) )
    
    myTests().main()