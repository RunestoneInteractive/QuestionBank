.. activecode:: ClassDiggingDeeperTest1
    :author: Wesley Thang
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: ClassesDiggingDeeper
    :subchapter: Exercises
    :topics: ClassesDiggingDeeper/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0
    :total_students_attempting: 1
    :num_students_correct: 1.0
    :mean_clicks_to_correct: 32.0

    Write a new Class definition called ``Complex`` to define a complex number object.
    
    The Complex class will have two instance variables: ``real`` and ``imag`` which
    are the real and imaginary values of the complex number.
    
    **Step 1.**  Define and initialize the object with the two input parameters (real and imag).
    ::
    
      c = Complex(3,4)     # creates the number (3 + 4i)
    
    **Step 2.**  Also create the following methods:
    
    ``getReal`` should **return** the the real value of the number
    
    ``getImag`` should **return** the the imaginary value of the number
    
    ``magnitude`` should **return** the magnitude of the number - the magnitude is square_root(r*r + i*i)
    
    **Step 3.**  The class should support Python's ``print()`` function.
    Don't worry about cases where the real or imaginary value is 0
    or negative.  It is OK to print out (-5i) as ``0 + -5i``
    
    ::
    
      c = Complex(3, 4)
      print(c)    #   will print out the string '3 + 4i'
      c = Complex(0, -5)
      print(c)    #   will print out the string '0 + -5i'
    
    
    **Step 4.**  Finally, the ``+`` operator should be supported by this class so that two complex numbers
    can be added like ``c1 + c2``. Ex.  (3 + 4i) + (6 + 10i) = (9 + 14i) where the real components
    are added and the imaginary components are added
    
    ~~~~
    class Complex:
    
    reate the constructor
     ...
    
    create the getReal()
     ...
    
    create the getImag()
     ...
    
    create the magnitude()
     ...
    
    service Python's print(complex_num)
     ...
    
    service Python's '+' operator so that c1 + c2 works for this class
     ...
    
    
    # Make your own test cases here
    
    ====
    
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def testOne(self):
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
    
    myTests().main()