.. activecode:: assess_ac3_1_1_8
   :author: bmiller
   :difficulty: 1.044732941
   :basecourse: fopp
   :chapter: Conditionals
   :subchapter: week3a1
   :topics: Conditionals/week3a1
   :from_source: T
   :language: python
   :autograde: unittest
   :practice: T
   :pct_on_first: 0.525297619
   :total_students_attempting: 672
   :num_students_correct: 503.0
   :mean_clicks_to_correct: 1.75944334

   Write code so that if ``"STATS 250"`` is in the list ``schedule``, then the string ``"You could be in Information Science!"`` is assigned to the variable ``resp``. Otherwise, the string ``"That's too bad."`` should be assigned to the variable ``resp``.
   ~~~~
   schedule = ["SI 106", "STATS 250", "SI 110", "ENGLISH 124/125"]
   
   =====
   
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
   
      def testOne(self):
         self.assertEqual(resp, "You could be in Information Science!", "Testing the value of resp given the schedule list provided.")
         self.assertIn("if", self.getEditorText(), "Testing that you used an if clause.")
   
   myTests().main()