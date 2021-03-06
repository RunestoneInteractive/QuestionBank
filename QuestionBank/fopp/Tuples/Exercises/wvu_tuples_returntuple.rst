.. activecode:: wvu_tuples_returntuple
    :author: Brian Powell
    :difficulty: 1.2685943775
    :basecourse: fopp
    :chapter: Tuples
    :subchapter: Exercises
    :topics: Tuples/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.1235955056
    :total_students_attempting: 89
    :num_students_correct: 50.0
    :mean_clicks_to_correct: 5.56

    The dictionary **majors** contains major codes as the key and major names as the value.
    
    Write a function named find_major() that takes one parameter, a major code. If the major code exists in **majors**, your function should return a tuple where the first value is the major code and the second is the name of the major. If the major code doesn't exist, return a tuple where the first value is ``None`` and the second is a string containing ``Error``.
    
    Print the name of the major with code 3084.
    ~~~~
    majors = {3084: 'Computer Science',
                3025: 'Electrical Engineering',
                3020: 'Computer Engineering',
                3027: 'Cybersecurity',
                3068: 'Biometric Systems Engineering'}
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(find_major(3084),(3084, "Computer Science"),"Computer Science is the associated major name")
           self.assertEqual(find_major(0),(None,"Error"), "Major code 0 should return Error")
    
    myTests().main()