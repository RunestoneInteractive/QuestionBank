.. activecode:: assess_ac_2_1_1_3
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Sequences
    :subchapter: week2a1
    :topics: Sequences/week2a1
    :from_source: T
    :autograde: unittest
    :language: python
    :practice: T

    Write code that combines the following variables so that the sentence "You are doing a great job, keep it up!" is assigned to the variable ``message``. Do not edit the values assigned to ``by``, ``az``, ``io``, or ``qy``.
    ~~~~
    by = "You are"
    az = "doing a great "
    io = "job"
    qy = "keep it up!"


    =====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def test_output(self):
        self.assertEqual(by, 'You are', "Testing original variables.")
        self.assertEqual(az, 'doing a great ', "Testing original variables.")
        self.assertEqual(io, 'job', "Testing original variables.")
        self.assertEqual(qy, 'keep it up!', "Testing original variables.")
        self.assertEqual(message, 'You are doing a great job, keep it up!', "Testing that the value of message is what was expected.")
        self.assertNotIn("You are doing a great job, keep it up!", self.getEditorText(), "Testing for hardcoding (Don't worry about actual and expected values).")


    myTests().main()