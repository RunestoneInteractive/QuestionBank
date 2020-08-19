.. activecode:: msuHonp105LetterLoop
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
    :mean_clicks_to_correct: 3.0384615385

    LETTER LOOP PROGRAM
    
    Currently, this program loops through all the letters in the English alphabet.  It also prints a message next to the first two vowels.
    
    1. Click SAVE AND RUN
        a. Examine the output.
        b. Examine the test results.  Notice that it fails some tests, because it does not meet the new specifications yet.
        
    2. THEN, MAKE THE FOLLOWING CHANGES TO THE PROGRAM:
        a. Make the message print for all of the remaining vowels. 
            i. Find the line that says if inLetter == "A" or inLetter == "E": 
                a. Change it to read if inLetter == "A" or inLetter == "E" or inLetter == "I" or inLetter == "O" or inLetter == "U":
                b. Take care not to accidentally remove the colon at the end.
    3. CLICK SAVE AND RUN AGAIN
        a. Examine the output
        b. Examine the test results.  Make sure it is 100 percent (no failures).
    4. Once it is working correctly, click the SCORE ME button. 
    
    ~~~~
    
    # Letter loop program
    # This program illustrates iteration using the FOR loop, as well as selection.
    # It also illustrates how we define and use a function, which takes input and produces output
    
    # Here we will define a function named isVowel
    # You need to change it so that it will return the correct results
    # It is only partially working
    # Notice that with functions there is a special way to document the function
    # The documentation for a function is started and ended with the triple single quotes
    def isVowel(inLetter):
       '''
       Determines if a character is a vowel.
    
               Parameters:
                       inLetter (str): A single character
    
               Returns:
                       outVowel (bool): True if the inLetter is a vowel; False otherwise
       '''
       # Within a function, we can also declare variables that are used by the function
       # Here is one called outValue.  It is implicitly Boolean because we assigned it a Boolean value
       # Notice that Boolean values are case sensitive
       # In out case, we will give it an initial value of False.  It will only be changed if certain conditions are met.
       outVowel = False
    
       # The if statement checks if some condition is true
       # Notice that we can use boolean operators to connect different conditions
       # The bottom line is - the entire expression must either evaluate to True of False
       # Then we can take some course of action based on whether the expression evaluates to True or not
       if inLetter == "A" or inLetter == "E":
           outVowel = True
       
       # Every function must have a return statement
       # This tells us what the output of the function will be
       # In pur case, we are returning the value of the outVowel boolean variable
       return outVowel
    # We are done defining our functions    
    # The following code is what will actually run    
    
    # Define a variable named alphabet, and assign it a value
    # It will implicitly be a string, because we are assigning it a value enclosed by quotes
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # The for loop can iterate over any variable type of a known length
    # The string we have already defined is of a particular length
    # So we can use the for loop to iterate over it, character by character how long the string is
    # With the FOR loop, you use a new variable to store each item retrieved from whatever other variable you are iterating over
    # In our instance it will keep running until we reach the last letter in the alphabet string variable
    for letter in alphabet:
       if isVowel(letter):
           print(letter + " This is a vowel") 
       else:
           print(letter)
    
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
      def testOne(self):
          self.assertEqual(isVowel("A"),True,"You missed a vowel.  Please double check.")
          self.assertEqual(isVowel("E"),True,"You missed a vowel.  Please double check.")
          self.assertEqual(isVowel("I"),True,"You missed a vowel.  Please double check.")
          self.assertEqual(isVowel("O"),True,"You missed a vowel.  Please double check.")
          self.assertEqual(isVowel("U"),True,"You missed a vowel.  Please double check.")
          self.assertEqual(isVowel("B"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("C"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("D"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("F"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("G"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("H"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("J"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("K"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("L"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("M"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("N"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("P"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("Q"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("R"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("S"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("T"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("V"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("W"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("X"),False,"Do mix up consonants with vowels.")
          self.assertEqual(isVowel("Z"),False,"Do mix up consonants with vowels.")
    myTests().main()
    
    ig values (conf.py):
    
    tivecode_div_class - custom CSS class of the component's outermost div
    tivecode_hide_load_history - if True, hide the load history button
    sm_uri - Path or Full URL to folder containing WASM files for SQL. /_static is default