.. activecode:: KDL_ch2_8
   :author: Kaelyn Leake
   :difficulty: 1.0
   :basecourse: fopp
   :chapter: SimplePythonData
   :subchapter: Exercises
   :topics: SimplePythonData/Exercises
   :from_source: F
   :language: python
   :autograde: unittest

   Create a variable named ``carname`` and assign the value 
   ``Honda`` to it. Then print how many characters ``carname`` 
   has. 
    
   Warning: you cannot write ``print(5)``
   ~~~~
   
   ====
   from unittest.gui import TestCaseGui
   import re
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(carname,"Honda",feedback="carname is correctly assigned")
           self.assertIn('len(carname)', self.getEditorText(), 'Contains correct command')
           self.assertTrue(re.search(str(len(carname))[:5], self.getOutput()), 'Checking answer.')
   myTests().main()