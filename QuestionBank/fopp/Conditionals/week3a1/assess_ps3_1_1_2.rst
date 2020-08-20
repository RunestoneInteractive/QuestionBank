.. activecode:: assess_ps3_1_1_2
    :author: bmiller
    :difficulty: 1.1485528847
    :basecourse: fopp
    :chapter: Conditionals
    :subchapter: week3a1
    :topics: Conditionals/week3a1
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T
    :pct_on_first: 0.3090234858
    :total_students_attempting: 809
    :num_students_correct: 613.0
    :mean_clicks_to_correct: 3.5220228385

    The variable ``sentence`` stores a string. Write code to determine how many words in ``sentence`` start and end with the same letter, including one-letter words.
    Store the result in the variable ``same_letter_count``.
    
    
    Hard-coded answers will receive no credit.
    ~~~~
    sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
    
    # Write your code here.
    
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(same_letter_count, 2, "Checking that same_letter_count has the correct value")
            self.assertIn('for ', self.getEditorText(), "Testing that your code has a for loop")
    myTests().main()