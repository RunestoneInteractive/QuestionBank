.. activecode:: LHSQuestionTen
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 1.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 1.0

    We have a dictionary of the specific events that Italy has won medals in and the
    number of medals they have won for each event. Assign to the variable ``events``
    a list of the keys from the dictionary ``medal_events``. Do not hard code this.
    
    ~~~~   
    medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
    
    # your code here to create the list events from the medal_events dictionary.
        
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
            self.assertEqual(sorted(events), sorted(['Shooting', 'Fencing', 'Judo', 'Swimming', "Diving"]), "Testing that events was created correctly")   
    
    myTests().main()