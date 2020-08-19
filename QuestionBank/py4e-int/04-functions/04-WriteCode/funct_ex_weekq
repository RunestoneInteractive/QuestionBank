.. activecode:: funct_ex_weekq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, …6=Sat, and a boolean indicating
    if we are on vacation, return a string of the form “7:00” indicating when the alarm clock
    should ring. Weekdays, the alarm should be “7:00” and on the weekend it should be “10:00”.
    Unless we are on vacation – then on weekdays it should be “10:00” and weekends it should be
    “off”.
    ~~~~
    def alarm_clock(day, vacation):
        # your code here

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(alarm_clock(1, False),'7:00',"Tested alarm_clock on input 1 and False")
            self.assertEqual(alarm_clock(5, False),'7:00',"Tested alarm_clock on input 5 and False")
            self.assertEqual(alarm_clock(0, False),'10:00',"Tested alarm_clock on input 0 and False")
            self.assertEqual(alarm_clock(6, False),'10:00',"Tested alarm_clock on input 6 and False")
            self.assertEqual(alarm_clock(0, True),'off',"Tested alarm_clock on input 0 and True")
            self.assertEqual(alarm_clock(6, True),'off',"Tested alarm_clock on input 6 and True")
            self.assertEqual(alarm_clock(1, True),'10:00',"Tested alarm_clock on input 1 and True")

    myTests().main()