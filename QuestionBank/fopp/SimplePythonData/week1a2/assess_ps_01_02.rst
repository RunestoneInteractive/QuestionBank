.. activecode:: assess_ps_01_02
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: SimplePythonData
    :subchapter: week1a2
    :topics: SimplePythonData/week1a2
    :from_source: T
    :language: python
    :autograde: unittest
    :practice: T

    Write code to assign the number of *characters* in the string ``rv`` to a variable ``num_chars``.
    ~~~~
    rv = """Once upon a midnight dreary, while I pondered, weak and weary,
        Over many a quaint and curious volume of forgotten lore,
        While I nodded, nearly napping, suddenly there came a tapping,
        As of some one gently rapping, rapping at my chamber door.
        'Tis some visitor, I muttered, tapping at my chamber door;
        Only this and nothing more."""

    # Write your code here!

    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

        def testOne(self):
           self.assertEqual(num_chars, len(rv), "Testing that num_chars has been set to the length of rv")

    myTests().main()