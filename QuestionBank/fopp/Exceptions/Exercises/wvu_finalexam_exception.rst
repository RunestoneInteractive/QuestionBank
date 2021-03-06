.. activecode:: wvu_finalexam_exception
    :author: Brian Powell
    :difficulty: 1.0656339644
    :basecourse: fopp
    :chapter: Exceptions
    :subchapter: Exercises
    :topics: Exceptions/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.2878787879
    :total_students_attempting: 66
    :num_students_correct: 35.0
    :mean_clicks_to_correct: 2.1142857143

    Add exception handling to the **get_value()** function so that it, if an IndexError exeception occurs because the specified index does not exist, the function returns the keyword ``None``. Do not handle any other types of exceptions.    
    
    ~~~~
    def get_value(data_list, index):
        return data_list[index]
    
    # Sample list data
    my_list = ['a', 'b', 'c']
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(get_value([0, 1, 2], 1), 1, "Correct value returned when index exists.")
            self.assertEqual(get_value([0, 1, 2], 3), None, "Correct value returned when index does not exist.")
    
            test_three = "try:" in self.getEditorText()
            self.assertEqual(test_three, True, "First part of exception handling in place.")
    
            test_four = "except IndexError:" in self.getEditorText()
            self.assertEqual(test_four, True, "Second part of exception handling in place.")
    
    myTests().main()