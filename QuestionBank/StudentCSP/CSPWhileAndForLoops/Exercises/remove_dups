.. activecode:: remove_dups
    :author: Barbara  Ericson
    :difficulty: 0.0
    :basecourse: StudentCSP
    :chapter: CSPWhileAndForLoops
    :subchapter: Exercises
    :topics: CSPWhileAndForLoops/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1007462687
    :total_students_attempting: 268
    :num_students_correct: 229.0
    :mean_clicks_to_correct: 11.4366812227

    Fix the code below to remove all adjacent duplicate values in the passed list.  For 
    example, removeDups([5, 5, 1]) returns [5, 1] and removeDups([1, 1, 2, 2, 3, 3, 3, 5, 6, 5, 6]) returns [1, 2, 3, 5, 6, 5, 6].  
    ~~~~
    def removeDups(a_list):
        prev = a_list[1]
        index = 2
        while index < len(a_list)
            if a_list[index] == prev:
                a_list.pop(index)
            else:
                prev = a_list[index]
            index += 1
        return a_list
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
             self.assertEqual(removeDups([5, 5, 1]), [5, 1], 'removeDups([5, 5, 1)')
             self.assertEqual(removeDups([1, 1, 2, 2, 3, 3, 3, 5, 6, 5, 6]), [1, 2, 3, 5, 6, 5, 6], 'removeDups([1, 1, 2, 2, 3, 3, 3, 5, 6, 5, 6])')
             self.assertEqual(removeDups([1, 2, 3, 3]), [1, 2, 3], 'removeDups([1, 2, 3, 3)')
             self.assertEqual(removeDups([5, 3, 1]), [5, 3, 1], 'removeDups([5, 3, 1)')
             self.assertEqual(removeDups([5, 5, 5]), [5], 'removeDups([5, 5, 5)')
             self.assertEqual(removeDups([5, 1, 1]), [5, 1], 'removeDups([5, 1, 1)')
    
    
              
    myTests().main()