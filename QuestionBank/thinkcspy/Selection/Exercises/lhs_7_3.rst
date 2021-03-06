.. activecode:: lhs_7_3
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Selection
    :subchapter: Exercises
    :topics: Selection/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.2293986637
    :total_students_attempting: 449
    :num_students_correct: 433.0
    :mean_clicks_to_correct: 11.143187067

    3 criteria must be taken into account to identify leap years:
    
    The year is evenly divisible by 4;
    
    If the year can be evenly divided by 100, it is NOT a leap year, unless;
    
    The year is also evenly divisible by 400. Then it is a leap year.
    
    Write a function that takes a year as a parameter and returns ``True`` if the year is a leap year, ``False`` otherwise.
    ~~~~
    def isLeap(year):
        # your code here
    
    
    def main():
        # try out a bunch of years
        for year in [ 2019, 2020, put_a_bunch_of_years_inside_here ]:
            print(year, ":", isLeap(year))
    
    if __name__ == "__main__":
        main()
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            print("Auto-testing...")
            self.assertEqual(isLeap(1944),True,"Tested isLeap on an input of 1944")
            self.assertEqual(isLeap(2011),False,"Tested isLeap on an input of 2011")
            self.assertEqual(isLeap(1986),False,"Tested isLeap on an input of 1986")
            self.assertEqual(isLeap(1800),False,"Tested isLeap on an input of 1800")
            self.assertEqual(isLeap(1900),False,"Tested isLeap on an input of 1900")
            self.assertEqual(isLeap(2000),True,"Tested isLeap on an input of 2000")
            self.assertEqual(isLeap(2056),True,"Tested isLeap on an input of 2056")
    
    myTests().main()