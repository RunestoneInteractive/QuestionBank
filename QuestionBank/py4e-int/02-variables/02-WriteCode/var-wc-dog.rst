.. activecode:: var-wc-dog
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 02-variables
    :subchapter: 02-WriteCode
    :topics: 02-variables/02-WriteCode
    :from_source: T
    :nocodelens:

    Assume that you have 24 slices of pizza and 7 people that are going to share it.
    There's been some arguments among your friends, so you've decided to only give people whole slices.
    Your pet dog Andy loves pizza. Write a Python expression with the modulus operator that calculates
    how many pizza slices will be left over for your dog after serving just whole slices to 7 people.
    Assign the result of that expression to ``forAndy``.

    ~~~~



    ====
    from unittest.gui import TestCaseGui
    class myTests(TestCaseGui):

        def testOne(self):
            self.assertEqual(forAndy,3)

    myTests().main()