.. activecode:: lhs_test3_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 105
    :num_students_correct: 17.0
    :mean_clicks_to_correct: 16.6470588235

    **Create a Complex Class**
    
    Write a new Class definition called ``Complex`` to define a complex number object.
    
    The Complex class will have **only** two instance variables: ``real`` and ``imag`` which
    are the real and imaginary **integer/float** values of the complex number. There should be no other instance
    variables besides these.
    
    **( 5 pts ) Step 1.**  Define and initialize the object with the two **integer/float** input parameters (real and imag)
    where the first parameter defines the ``real`` attribute and the second parameter
    defines the ``imag`` attribute of the ``Complex`` object.  So, ``Complex(1,2)`` should create the Complex object ``1 + 2i``
    
    Using the class you have defined, make the complex number (3 + 4i) and assign it to
    the variable ``c1``.  Make another complex number (6 + 10i) and assign it to the variable ``c2``.
    
    **( 10 pts ) Step 2.**  Also create the following methods:
    
    ``getReal()`` should **return** the the real value of the number
    
    ``getImag()`` should **return** the the imaginary value of the number
    
    ``magnitude()`` should **return** the magnitude of the number - the magnitude is square root of (r*r + i*i).
    Remember, you can use ``x ** 0.5`` to get the square root of x.
    
    ``conjugate()`` should **return** a Complex number which is the conjugate of itself. The conjugate of
    a Complex number merely negates the ``imag`` value. So, the conjugate of (3 + 4i) is (3 - 4i). Note that
    the object itself does not change, but it returns a Complex number.
    
    Using the method you just defined, make a variable ``m1`` to be the magnitude of c1.
    Using the method you just defined, make a variable ``c3`` to be the conjugate of c2.
    
    **( 4 pts ) Step 3.**  You should also create the appropriate method so that printing the number will 
    print out the following:
    
    Ex. ``print(c1)`` will print out as ``3 + 4i``. Don't worry about 0 or negative numbers.  It is OK
    for (-5i) to be printed out as ``0 + -5i``
    
    **( 4 pts ) Step 4.**  Finally, the ``+`` operator should be supported by this class so that two complex numbers
    can be added like ``c1 + c2``. Ex.  (3 + 4i) + (6 + 10i) = (9 + 14i) where the real components
    are added and the imaginary components are added. So, a Complex number should be the result of the ``+`` operator.
    
    ~~~~
    # create Complex class
    
    reate the consturctor
    
    create the getReal()
    
    create the getImag()
    
    create the magnitude()
    
    service Python's print(complex_num)
    
    service Python's '+' operator so that c1 + c2 works for this class
    
    # Make your own test cases here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
            SelfTest = False
            if (SelfTest):
                self.assertEqual(0,1,"Auto-testing if OFF - you must check the program yourself for now")
                return
            
            print("Auto-Testing...")
    
            # Step 1 - Test c1 and c2 object creation w/ proper names
            self.assertEqual(c1.real, 3, "Testing real variable")
            self.assertEqual(c1.imag, 4, "Testing imag variable")
            self.assertEqual(c2.real, 6, "Testing real variable")
            self.assertEqual(c2.imag, 10, "Testing imag variable")
    
            # Step 2 - Methods
            self.assertEqual(c2.getReal(), 6, "Testing getReal()")
            self.assertEqual(c2.getImag(), 10, "Testing getImag()")
            self.assertEqual(m1, 5, "Testing magnitude()")
            self.assertEqual(Complex(5,12).magnitude(), 13, "Testing magnitude with another number")
            self.assertEqual(c3.real, 6, "Testing real variable of conjugate")
            self.assertEqual(c3.imag, -10, "Testing imag variable of conjugate")
            self.assertEqual(c2.real, 6, "Testing that c1 is still the same")
            self.assertEqual(c2.imag, 10, "Testing that c1 is still the same")
    
            # Step 3 - __str__
            self.assertEqual(c1.__str__().replace(" ",""), "3+4i", "Testing __str__()")
            self.assertEqual(Complex(6, 9).__str__().replace(" ",""), "6+9i", "testing __str__()")
    
            # Step 4 - Addition using __add__()
            cx = Complex(2,3)
            cy = Complex(7,10)
            cadd = cx + cy
            self.assertEqual(cadd.getReal(), 9, "Testing real portion of +")
            self.assertEqual(cadd.getImag(), 13, "Testing imag portion of +")
            self.assertEqual(cx.real, 2, "Testing cx did not change")
            self.assertEqual(cy.imag, 10, "Testing cy did not change")
    
    myTests().main()