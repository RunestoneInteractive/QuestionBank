.. parsonsprob:: unittest1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPIntroData
   :subchapter: Exercises
   :topics: CSPIntroData/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0885416667
   :total_students_attempting: 192
   :num_students_correct: 151.0
   :mean_clicks_to_correct: 13.582781457

   Put the blocks in order to create a testing class TestCar with a setUp method that creates a car object, 
   then the test_get_make, and finally the test_set_make (in that order).
   -----
    import unittest
    import car
   =====
    class TestCar(unittest.TestCase):
   =====
    class TestCar(): #paired
   =====
        def setUp(self):
   =====
            self.c = Car("Ford","Volt", "Blue") 
   =====
        def test_get_make(self):
   =====
        def t_get_make(self):  #paired
   =====
            self.assertEqual(self.c.get_make(),"Ford")
   =====
            self.assertEqual(c.get_make(),"Ford") #paired
   =====
        def test_set_make(self):
   =====
            self.c.set_make("Honda")
   =====
            self.assertEqual(self.c.get_make(),"Honda")
   =====
            self.assertFalse(self.c.get_make(),"Honda") #paired
   =====
    unittest.main(verbosity=2)