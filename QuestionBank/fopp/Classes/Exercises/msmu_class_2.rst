.. activecode:: msmu_class_2
    :author: Irma Ravkic
    :difficulty: 1.1862585477
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.037037037
    :total_students_attempting: 54
    :num_students_correct: 37.0
    :mean_clicks_to_correct: 4.1621621622

    Consider the class below. Write the main part of the program that asks the users for input and uses those inputs to create a new instance of ``User`` and store it in variable ``new_user``.
    
    1. Ask for the user's username and assign to variable `username`
    
    2. Ask for the user's email and assign it to variable `email`
    
    3. Ask for the user's year of birth and store it in variable `yob`
    
    4. Create a new object with those value the user provided. Assign the new object to variable `new_user`
    ~~~~
    class User:
       def __init__(self, username, email, YOB):
          self.username = username
          self.email = email
          self.YOB = YOB
    
    #your code here   
          
    
    ====
    from unittest.gui import TestCaseGui
    import re    
    
    class myTests(TestCaseGui):
        def testOne(self):
            pattern1 = r'(input\(.+\))'
            pattern2 = r'new_user\s*=\s*User\s*\(\w*,\s*\w+\s*,\s*(int\(\w*\)|\w*)\s*\)'
            self.assertEqual(True, bool(re.findall(pattern1, self.getEditorText())), "You need to use input() to get input from the user.")
            self.assertEqual(True, bool(re.findall(pattern2, self.getEditorText())), "You need to create an instance of the class and assign to variable called new_user")
            self.assertEqual(True, hasattr(new_user, 'username'), "You need to define username property in your class.")
            self.assertEqual(True, hasattr(new_user, 'email'), "You need to define email property in your class.")
            self.assertEqual(True, hasattr(new_user, 'YOB'), "You need to define YOB property in your class.")
            self.assertEqual(True, type(new_user.YOB) is int, "Year of birth is a number and therefore its type needs to be integer (int)")
            self.assertEqual(True, new_user.YOB == yob, "Object's YOB needs to be the same as the input provided")
            self.assertEqual(True, new_user.username == username, "Object's username needs to be the same as the input provided")
            self.assertEqual(True, new_user.email == email, "Object's email needs to be the same as the input provided")
        
            
    myTests().main()