.. activecode:: msuHonp105NumberLoop
    :author: James Williams
    :difficulty: 0.0
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
    :mean_clicks_to_correct: 2.9615384615

    NUMBER LOOP PROGRAM
    
    This program currently produces a list of whole integer multiples of 3, starting with 0 and stopping at 9.
    Next to each integer, a message is printed next to each even integer.
    
    1. Click SAVE AND RUN
        a. Examine the output.
        b. Examine the test results.  Notice that it fails some tests, because it does not meet the new specifications yet.
        
    2. THEN, MAKE THE FOLLOWING CHANGES TO THE PROGRAM:
        a. Make the sequence go up to and including 30. 
            i. Find the line that says while myNumber < 10:
                a. Change it to read while myNumber < 31:
                b. Take care not to accidentally remove the colon at the end.
        b. Print a message next to each odd number instead of each even number.
            i. Find the line that says if inNumber%2==0:
                a. Change it to read if inNumber%2==1:
                b. Take care not to accidentally remove the colon at the end.
            ii. Find the line that says outMessage = "This number is even."
                a. Change it to read outMessage = "This number is odd."
    3. CLICK SAVE AND RUN AGAIN
        a. Examine the output
        b. Examine the test results.  Make sure it is 100 percent (no failures).
    4. Once it is working correctly, click the SCORE ME button. 
    
    ~~~~
    #-----------------------------------------------
    # Number Loop Program
    # This program ilustrates iteration using the "while" loop, as well as selection.
    # We also get to do some things with strings and integers.
    # It also illustrates how we define and use a function.
    #-----------------------------------------------
    
    #-----------------------------------------------
    # All function definitions need to happen before the code that will run.
    
    # Here, we define a function called createMessage.  
    # You need to change it so that it will return a message for odd numbers
    # Right now it returns a message for even numbers
    # Notice documentation for a function is started and ended with the triple single quotes
    def createMessage(inNumber):
        '''
        Produces a message for a number, based on certain business rules defined.
    
                Parameters:
                        inNumber (int): A single integer
    
                Returns:
                        outMessage (str): A character string containing a message.
        '''
        # We define a variable to store the message we will produce.  The message starts off as an empty string
        outMessage=""
        
        # Right now this conditional statement checks if a number is even.
        # This is done with the modulus operator.
        # THe condition now reads: if the given number is divided by 2, is the remainder equal to 0?  True or False?
        # Notice we use the equality == operator to compare the values.  Be careful - the equality operator is ==, not = 
        # If you divide any integer by 2, the remainder can only be 0 or 1.
        # If it is a 0, the integer is even.  If it is 1, then the integer is odd.
        # *** YOU HAVE TO CHANGE THIS CONDITION TO CHECK IF A NUMBER IS ODD - SO CHANGE THE 0 on the right side of the equality operator to a 1 ***
        if inNumber%2==0:
            # We will only produce a non-empty message if the conditional rule is satisfied.  Otherwise it will remain blank.
            # Remember that we will be changing the conditional rule.  So for the message to make sense ...
            # *** YOU ALSO HAVE TO CHANGE WHAT THE MESSAGE SAYS. ***  Just change the word "even" to "odd" - and leave everything else exactly as it is.
             outMessage = "This number is even."
        # We return the value of the message to whatever piece of code made a "call" to this function
        return outMessage
    
    
    def runNumberLoop(inTrue):
        '''
        This function actually runs the loop.  Since this is for learning purposes, we set it up as a function so we can look at certain metrics
    
                Parameters:.
                        a placeholder boolean value - we need this or else the function would execute as soon as the program runs - for this exercise this is not what I want
    
                Returns:
                        a list of integers - the first is the number of times the loop ran, and the second is the value that caused the loop to exit
        '''
        # We define a variable named myCounter.  THis will track how many times the loop executes.
        myCounter = 0
        # We define a variable named myNumber and assign it an initial value.
        # Notice that this is a numeric variable, because of the value we assigned to it.
        myNumber = 0
    
        # Our "while" loop will create a sequence of integers starting at 0 and increasing by 3 with each turn of the loop
        # The incrementation happens at the end of the loop
        # Please note that "while" loops can increment however we want them to - depending on how we program it.
        # But this also means we need define condition for the loop to end!
    
        # Right now the numeric sequence will only go up to 9
        # This is becuase the "while" loop condition has been defined as myNumber < 10,
        #    and since we started at 0 and are incrementing by 3, the last number that will match this rule is 9.
        # *** YOU HAVE TO CHANGE THIS SO THAT THE NUMERIC SEQUENCE WILL GO UP TO AND INCLUDE 30 ***
        while myNumber < 10:
        
            # Increment the myCounter variable by 1.  This way we can use this later on to check how many times the loop ran.
            myCounter = myCounter + 1
    
            # For the given number in the sequence, we store the message in a string variable named myMessage
            myMessage = createMessage(myNumber)
    
            # Check if the message is empty or not.
            # If it is not, then we print a space and the message after the number
            # Notice we have to convert the variable myNumber to a string first
            # Then we can use the plus sign to combine strings together
            if len(myMessage)>0:
                print(str(myNumber) + " * " + myMessage)
            else:
               print(str(myNumber))
                     
            # Increment the value of myNumber by 3.  We have to make sure the loop will eventually end!
            myNumber = myNumber + 3
    
        # This is the end of the loop
        return [myCounter, myNumber]
    
    #-----------------------------------------------
    # We are done defining our functions.
    # Now we write the code that wil actually run
    
    # We just call the runNumberLoop function
    runNumberLoop(True)
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
      def testOne(self):
          self.assertEqual(createMessage(0),"","You have to change the rules for odd/even - no message for even")
          self.assertEqual(createMessage(3),"This number is odd.","Make sure the odd message displays exactly as specified.")
          self.assertEqual(runNumberLoop(True),[11, 33],"Make sure the loop executes the correct number of times and increments by three each time")
    myTests().main()
    
    ig values (conf.py):
    
    tivecode_div_class - custom CSS class of the component's outermost div
    tivecode_hide_load_history - if True, hide the load history button
    sm_uri - Path or Full URL to folder containing WASM files for SQL. /_static is default