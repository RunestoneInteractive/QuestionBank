.. activecode:: funct_ex_nameq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Fix the errors on line 2 so the function ``nameAndAge`` returns
    the string "My name is **name** and I am **age** years old." The function
    call below should print "My name is John and I am 18 years old."
    ~~~~
    def nameAndAge(nameString, ageInt):
        return(My name is "nameString" and I am + "str(ageInt)" + years old.)

    print(nameAndAge("John", 18))

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(nameAndAge("John", 18),"My name is John and I am 18 years old.","Checks if the returned strings are equal.")

    myTests().main()