.. activecode:: asu_cs_ch04_ex4
    :author: Erdogan Dogdu
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: PythonTurtle
    :subchapter: Exercises
    :topics: PythonTurtle/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.5
    :total_students_attempting: 16
    :num_students_correct: 11.0
    :mean_clicks_to_correct: 2.3636363636

    Write a program to draw a hexagon with 6 triangles as shown here:
    
    https://i.stack.imgur.com/WLpfx.png
    
    Use two ``for`` loops and two ``range`` function.
    
    Hint: Draw 6 isosceles triangles (all sides of equal sizes), and each with 3 sides :)
    
    ~~~~
    # write your code here
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def testMany(self):
            outText = self.getOutput()
            editText = self.getEditorText()
            
            self.assertEqual(2, editText.count('for '), "You need to use just two 'for' loops!")
            self.assertEqual(2, editText.count('range('), "You need to use just two range functions!")
        
    myTests().main()