.. activecode:: msmu_class_1
    :author: Irma Ravkic
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 16
    :num_students_correct: 5.0
    :mean_clicks_to_correct: 23.2

    Hey there! Write code that makes a class called ``Pet``. This class should have the following attributes: ``name``, ``age`` and ``sound``.
    This means that each pet you create should have a name, age and sound it makes. Then do the following in the order given. Make sure each question works until proceeding to the next one:
    
    1. Define the initializer method ``__init__`` that will set the properties of your pets. 
       ``sound`` property should be "argh" by default. It should also set a new class variable
       called ``amount_of_energy`` to `0`.
    
    2. In the main program create an instance of ``Pet`` and assign it to a variable
       called ``my_pet`` with the following attributes: ``name`` is "Spock", ``age`` is 10.
    
    3. To your ``Pet`` class add a method called ``feed_me`` that takes one input called ``amount``, an integer representing the amount of food for feeding. ``feed_me`` should increment the ``amount_of_energy`` property of the class by the amount 
       ``amount`` **only if that amount is smaller or equal than 10**. Otherwise it prints: "Too much food" and doesn't change the amount of energy.
    
    4. Add a ``__repr__`` method that will print the following "My Pet" and the amount of energy your pet currently has. For example, "My Pet. Amount of energy = 100". Beware: 100 is fixed, and you should make it **variable** depending on how much energy your pet currently has.
    
    5. To your ``Pet`` class add a method called ``play`` that takes one input called ``amount``, an integer representing the amount of play. ``play`` should **decrement** the ``amount_of_energy`` property of the class by 
       ``amount`` **only if that amount is smaller or equal than** ``amount_of_energy`` (your pet cannot play if it requires more energy than it has). Otherwise it prints: "Not enough energy" and doesn't change the amount of energy.
    
    6. In your main program, call method ``feed_me`` on ``my_pet`` with ``amount = 5``. Print object ``my_pet``. Look at the amount of energy there? Did it change/increase from the initial `0`?
    7. In your main program, call method ``play`` on ``my_pet`` with ``amount = 2``. Print object ``my_pet``. Look at the amount of energy there? Did it change/decrease from the previous print? 
    ~~~~
    #your code here
    
    ====
    from unittest.gui import TestCaseGui
    import re    
    
    class myTests(TestCaseGui):
        def testOne(self):
            pattern1 = r'(sound\s*=\s*[\"|\']\w+[\"|\'])'
            pattern2 = r'((\"|\')+Spock(\"|\')+)'
            pattern3 = r'(self.amount_of_energy\s+=\s+0)'
            self.assertEqual(True, "class Pet:" in self.getEditorText(), "1. Make sure you defined your class in the following template: class class_name: ")
            self.assertEqual(True, "def __init__(self," in self.getEditorText(), "1. Make sure you defined __init__ method with all the attributes that constitute a Pet. Please look back to Section 20.4")
            self.assertEqual(True, bool(re.findall(pattern1, self.getEditorText())), "1. Make sure you set your sound variable to a default value provided in the assignment text.")
            self.assertEqual(True, "self.name = " in self.getEditorText(), "1. Make sure you set self.name with its associated variable name provided in the __init__ function.")
            self.assertEqual(True, "self.age = " in self.getEditorText(), "1. Make sure you set self.age with its associated variable name provided in the __init__ function.")
            self.assertEqual(True, "self.sound = " in self.getEditorText(), "1. Make sure you set self.sound with its associated variable name provided in the __init__ function.")
            self.assertEqual(True, bool(re.findall(pattern3, self.getEditorText())), "1. Make sure you set the amount of energy to 0!")
            self.assertEqual(True, my_pet.name == "Spock", "2. Make sure your pet (my_pet) is called Spock.")
            self.assertEqual(True, bool(re.findall(pattern2, self.getEditorText())), "2. Make sure you made Spock a string!")
        def testTwo(self):
            pattern4 = r'(def feed_me\(self\s?,\s?amount\s?\):)'
            pattern5 = r'(self.amount_of_energy\s-=\s+amount)'
            pattern6 = r'(self.amount_of_energy\s*=\s*self.amount_of_energy\s*\-\s*amount)'
            pattern7 = r'(def \_{2,2}repr\_{2,2}\(self\):)'
            pattern8 = r'(print\(\s*my_pet\s*\))'
            
            self.assertEqual(True, hasattr(my_pet, 'feed_me'), "3. Make sure you created the feed_me function in your Pet class.")
            
            self.assertEqual(True, bool(re.findall(pattern4, self.getEditorText())), "3. Make sure you defined your feed_me function correctly. Watchout on self and :")
            self.assertEqual(True, bool(re.findall(pattern7, self.getEditorText())), "4. Make sure you wrote the __repr__ method in your Pet class.")
            self.assertEqual(True, hasattr(my_pet, 'play'), "5. Make sure you created the play function in your Pet class.")
            self.assertEqual(True, (bool(re.findall(pattern5, self.getEditorText())) or bool(re.findall(pattern6, self.getEditorText()))), "5. Make sure you're decreasing the energy amount by the amount provided parameter amount of function play()")            
            self.assertEqual(True, bool(re.findall(pattern8, self.getEditorText())), "You need to print your my_pet object at least once in your main program. It needs to show the current amount of energy your pet has.")
            self.assertEqual(True, my_pet.amount_of_energy == 3, "6. Make sure that the final amount of energy of your pet is 3. You fed it 5 units, and then played with 2. So, 5 - 2 = 3. So your pet finally has 3 units of energy.")
    myTests().main()