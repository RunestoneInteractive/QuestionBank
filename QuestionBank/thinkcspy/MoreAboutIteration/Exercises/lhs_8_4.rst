.. activecode:: lhs_8_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: MoreAboutIteration
    :subchapter: Exercises
    :topics: MoreAboutIteration/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0284552846
    :total_students_attempting: 492
    :num_students_correct: 445.0
    :mean_clicks_to_correct: 17.6404494382

    Write a function ``drugPotency(loss, expire)`` that determines how many months a drug
    can remain in storage given a potency loss percentage (``loss``) and an expiration
    target (``expire``). For example, if a certain drug looses 4% of its effectiveness
    every month it is in storage, when its effectiveness is below 50% it is considered expired
    and must be discarded. The output from ``drugPotency(4.0, 50.0)`` would be::
    
        Month: 0    effectiveness: 100.0
        Month: 1    effectiveness: 96.0
        Month: 2    effectiveness: 92.16
        Month: 3    effectiveness: 88.4736
        Month: 4    effectiveness: 84.934656
        Month: 5    effectiveness: 81.53726976
        Month: 6    effectiveness: 78.2757789696
        Month: 7    effectiveness: 75.1447478108
        Month: 8    effectiveness: 72.1389578984
        Month: 9    effectiveness: 69.2533995824
        Month: 10   effectiveness: 66.4832635992
        Month: 11   effectiveness: 63.8239330552
        Month: 12   effectiveness: 61.270975733
        Month: 13   effectiveness: 58.8201367037
        Month: 14   effectiveness: 56.4673312355
        Month: 15   effectiveness: 54.2086379861
        Month: 16   effectiveness: 52.0402924666
        Month: 17   effectiveness: 49.958680768 DISCARDED
    
    **HINT:** There is a tab used **right before** (without a space) the word "effectiveness" to print nicely. See 8.10 on how to make the tab character.
    So, you would have ``"\teffectiveness:"`` in your print statement.
    
    **HINT:** Also, make sure that you have 100.0, not 100 in the first output line... Make sure you have spelled the words correctly too.
    
    
    ~~~~
    def drugPotency(loss, expire):
        # your code here
        
        
    def main():
        drugPotency(4.0, 50.0)
    
    if __name__ == "__main__":
        main()
        
    ====
    import random
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def _drugPotency(self, loss, expire):
            month = 0
            effectiveness = 100.0
            outStr = "Month: " + str(month) + "\teffectiveness: " + str(effectiveness)
            while effectiveness > expire:
                outStr += "\n"
                effectiveness = effectiveness - (loss/100 * effectiveness)
                month += 1
                outStr += "Month: " + str(month) + "\teffectiveness: " + str(effectiveness)
            outStr += " DISCARDED\n"
            return outStr
    
        def testOne(self):
            print("\nAuto-testing...")
    
            loss = 9.0
            exp = 60.0
            expected = self._drugPotency(loss, exp)
            #print(expected)
            oLen = len(self.getOutput())
            drugPotency(loss, exp)
            oLenTest = len(self.getOutput())
            actual = self.getOutput()[oLen:oLenTest]  #extract new output
    
            expected = " ".join(expected.split()) 
            actual = " ".join(actual.split()) # remove extra spaces in the output
    
            self.assertEqual(actual, expected, "checking output for drugPotency(" + str(loss) + ", " + str(exp) + ")")
    
            loss = float(random.randrange(4,12))
            exp = float(random.randrange(50,65))
            expected = self._drugPotency(loss, exp)
            #print(expected)
            oLen = len(self.getOutput())
            drugPotency(loss, exp)
            oLenTest = len(self.getOutput())
            actual = self.getOutput()[oLen:oLenTest]  #extract new output
    
            expected = " ".join(expected.split()) 
            self.assertIn("\teffectiveness", actual, "Checking tab usage to make table")
    
            actual = " ".join(actual.split()) # remove extra spaces in the output
    
            self.assertEqual(actual, expected, "checking output for drugPotency(" + str(loss) + ", " + str(exp) + ")")
    
    myTests().main()