.. activecode:: funct_ex_tripq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-WriteCode
    :topics: 04-functions/04-WriteCode
    :from_source: T
    :practice: T
    :autograde: unittest

    Change the code below to create a function ``tripCost`` that calculates the cost of a trip.
    It should take the ``miles``, ``milesPerGallon``, and ``pricePerGallon`` as parameters and
    should return the cost of the trip.
    ~~~~
    miles = 500
    milesPerGallon = 26
    numGallons = miles / milesPerGallon
    pricePerGallon = 3.45
    total = numGallons * pricePerGallon
    print(total)

    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(tripCost(100, 25, 2.24),8.96,"Tested tripCost on inputs 100, 25, and 2.24")
            self.assertEqual(tripCost(250, 20, 3.01),37.625,"Tested tripCost on inputs 250, 20, and 3.01")

    myTests().main()