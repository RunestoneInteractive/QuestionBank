.. activecode:: LHSQuestionThirteen
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

    Provided is a dictionary called ``US_medals`` which has the first 70 metals that the
    United States has won in 2016, and in which category they have won it in. Using
    dictionary mechanics, assign the value of the key ``''Fencing''`` to a variable
    ``fencing_value``. Remember, do not hard code this.
    
    
    ~~~~   
    US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
    
    # your code here to assign the value of the key Fencing to a variable
    # fencing_value from the US_medals dictionary.
        
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testOne(self):
           self.assertEqual(fencing_value, US_medals.get("Fencing"), "Testing that fencing_value was set correctly.")        
    
    myTests().main()