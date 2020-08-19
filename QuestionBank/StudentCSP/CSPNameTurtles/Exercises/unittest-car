.. parsonsprob:: unittest-car
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1777777778
   :total_students_attempting: 135
   :num_students_correct: 133.0
   :mean_clicks_to_correct: 6.7744360902

   Put the code in order to define a TestCar class.  It should import unittest, then create the class.  Next it should define the setUp, test_get_model, and test_set_model methods. 
   -----
   import unittest
   =====
   class TestCar(unittest.TestCase):
   =====
       def setUp(self):
   =====
       def setUp(): #paired
   =====
           self.c = Car("Ford","Volt", "Blue") 
   =====
           c = Car("Ford","Volt", "Blue") #paired
   =====
       def test_get_model(self):
   =====
           self.assertEqual(self.c.get_model(), "Volt")
   =====
           self.assertEqual(c.get_model(), "Volt") #paired
   =====
   
       def test_set_model(self):
   =====
           self.c.set_model("Focus")
   =====
           c.set_model("Focus") #paired
   =====
           self.assertEqual(self.c.get_model(),"Focus")