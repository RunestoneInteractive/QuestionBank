.. activecode:: msuHonp105Calculator
    :author: James Williams
    :difficulty: 2.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: Exercises
    :topics: Labs/Exercises
    :from_source: F
    :autograde: unittest
    :language: python
    :pct_on_first: 0.0
    :total_students_attempting: 26
    :num_students_correct: 26.0
    :mean_clicks_to_correct: 4.5384615385

    CALCULATOR PROGRAM
    
    This program takes two operands and an operator as input from the user.
    It will then write the result to the screen.
    Currently, this program only accounts for the + and - operators.  It also has no error checking and is prone to run-time errors.  This would be an example of a starter program that would require refinements later on.
    
    1. Click SAVE AND RUN
        a. Enter input and examine the output.
        b. Notice that it cannot multiply, and that it is possible to enter garbage in and cause runtime errors
        c. Also, examine the test results.  You will see that the test case for multiplication fails. 
        
    2. THEN, MAKE THE FOLLOWING CHANGES TO THE PROGRAM:
        a. Make the calculator also perform multiplication. 
            i. Find the two lines that that says elif inOperator=="-":   , followed by ,  outResult = inOperand1 - inOperand2
                a. Take careful note of how these two lines are indented. Tnis is very important. 
                b. Copy those two lines as a single block, including the indents.
                c. Paste those lines directly before the line that says return outResult .  Do not overwrite anything!
                d. In the NEW lines you just pasted, change then to say elif inOperator=="+":   , followed by ,  outResult = inOperand1 * inOperand2
    3. CLICK SAVE AND RUN AGAIN
        a. Try addition, subtraction, and multiplication this time.  Make sure they all work.
        b. Examine the test results.  Make sure it is 100 percent (no failures).
    4. Once it is working correctly, click the SCORE ME button. 
    
    ~~~~
    #-----------------------------------------------
    # Calculator Program
    # This program ilustrates how we collect input from a user.
    # It also illustrates how we use multiple selection conditions
    #-----------------------------------------------
    
    #-----------------------------------------------
    # All function definitions need to happen before the code that will run.
    
    # Here, we define a function called calculateResult.  
    # You need to change it so that it allows for multiplication
    # Right now it only accounts for addition and subtraction
    # Notice documentation for a function is started and ended with the triple single quotes
    def calculateResult(inOperand1, inOperator, inOperand2 ):
        '''
        Given two operands and an operator, produces a calculated result.  There is no error chaecking in place yet, so we may have runtime errors.
    
                Parameters:
                        inOperand1 (float): A single integer (the top number)
                        inOperator (str): A mathematical operator symbol
                        inOperand2 (float): A single integer (the bottom number)
    
                Returns:
                        outResult (float): The result of the calculation, or a Null if calculation cannot happen.
        '''
        # We define a variable to store the result.  This starts off as a string XXX.  
        # If a calculation happens correctly, it will be a float instead.
        # In Python, we can dynamically change the type of a variable
        outResult=None
    
        if inOperator=="+":
            outResult = inOperand1 + inOperand2
        elif inOperator=="-":
            outResult = inOperand1 - inOperand2
        
        return outResult
        
        
    
    
    #-----------------------------------------------
    # We are done defining our functions.
    # Now we write the code that wil actually run
    
    myOperand1 = float(input("Enter a number: "))
    myOperator = input("Enter an operator: ")
    myOperand2 = float(input("Enter another number: "))
    
    myResult = calculateResult(myOperand1, myOperator, myOperand2)
    
    print('The result of ', myOperand1,  ' ', myOperator, ' ', myOperand2, ' is ', myResult, '.', sep='')
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
      def testOne(self):
          self.assertEqual(calculateResult(5, "+", 6),11,"Make sure addition is working correctly")
          self.assertEqual(calculateResult(5, "-", 6),-1,"Make sure subtraction is working correctly")
          self.assertEqual(calculateResult(5, "*", 6),30,"Make sure multiplication is working correctly")
    myTests().main()
    
    ig values (conf.py):
    
    tivecode_div_class - custom CSS class of the component's outermost div
    tivecode_hide_load_history - if True, hide the load history button
    sm_uri - Path or Full URL to folder containing WASM files for SQL. /_static is default