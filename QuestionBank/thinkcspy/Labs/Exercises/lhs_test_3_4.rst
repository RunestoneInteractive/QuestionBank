.. activecode:: lhs_test_3_4
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.196969697
    :total_students_attempting: 132
    :num_students_correct: 80.0
    :mean_clicks_to_correct: 5.1125

    **Create a Complex Class**
    
    Write a new Class definition called ``Complex`` to define a complex number object.
    
    Here is an example:  ``(3 + 4i)`` is a complex number with 3 as the Real value and 4 as the
    Imaginary value.
    
    The Complex class will have **only** two instance variables: ``real`` and ``imag``. These are
    **integer/floating point** values which are the real and imaginary values of the complex number. 
    There should be no other instance variables besides these.
    
    **( 5 pts ) Step 1.**  Define and initialize the object with the two input parameters (real and imag)
    where the first parameter defines the ``real`` attribute and the second parameter
    defines the ``imag`` attribute of the ``Complex`` object.
    
    Using the class you have defined, make the complex number (3 + 4i) and assign it to
    the variable ``c1``.  Make another complex number (6 + 10i) and assign it to the variable ``c2``.
    
    **( 10 pts ) Step 2.**  Also create the following methods:
    
    ``getReal()`` should **return** the the real value of the number
    
    ``getImag()`` should **return** the the imaginary value of the number
    
    ``magnitude()`` should **return** the magnitude of the number - the magnitude is square root of (r*r + i*i),
    where ``r`` represents the real component of the number and ``i`` represents the imaginary component value.
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
    are added and the imaginary components are added. 
    
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
    import sys
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
    
            # hide print()
            fname = "test.out"
            sys.stdout = open(fname, "w")
            
            print("Auto-Testing...")
    
            # Make an object
            c1 = Complex(5, 12)
            c2 = Complex(2, 6)
    
            self.assertEqual(c1.real, 5, "Testing real variable")
            self.assertEqual(c1.imag, 12, "Testing imag variable")
            self.assertEqual(c2.getReal(), 2, "Testing getReal()")
            self.assertEqual(c2.getImag(), 6, "Testing getImag()")
            self.assertEqual(c1.__str__(), "5 + 12i", "Testing __str()__")
            self.assertEqual(round(c1.magnitude(),5), round(13,5), "Testing magnitude()")
            self.assertEqual(round(c2.magnitude(),5), round((40)**0.5,5), "Testing magnitude()")
            c3 = c1 + c2
            self.assertEqual(c3.getReal(), 7, "Testing real portion of +")
            self.assertEqual(c3.getImag(), 18, "Testing imag portion of +")
    
            self.deleteFile(fname)
    
        # just opening and closing file does not work, so need a print statement to "empty" the file
        def deleteFile(self, fname):
            # empty out the file so nothing shows
            sys.stdout = open(fname, "w")
            print()
            sys.stdout.close()
    
    myTests().main()