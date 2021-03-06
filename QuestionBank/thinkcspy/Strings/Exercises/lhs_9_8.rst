.. activecode:: lhs_9_8
    :author: LHS CS Team
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest
    :pct_on_first: 0.0665024631
    :total_students_attempting: 406
    :num_students_correct: 380.0
    :mean_clicks_to_correct: 16.7052631579

    Write a function ``wheelOfFortune(letter, phrase)`` that plays one guess of the a ``letter``
    within a ``phrase``. The ``letter`` is a single character (that may be upper or lower case).
    The ``phrase`` is a string that is of any length with upper and lower case letters.
    
    The function should ignore the case of either the letter or the characters in the phrase.
    
    The function prints out the following messages:
    
    Example: wheelOfFortune('a', 'Hello World')
    
    ::
    
      Sorry, there is no "a"
    
    Example: wheelOfFortune('w', 'Hello World')
    
    ::
    
      There was 1 w found
      Found at position 6
    
    Example: wheelOfFortune('L', 'Hello World')
    
    ::
    
      There were 3 l's found
      Found at position 2
      Found at position 3
      Found at position 9
    
    **NOTE:** When you print out the first line of how many letters are found, you should
    print out the letter in lower case always.
    ~~~~
    # My Name:
    
    # define the wheelOfFortune(letter, phrase) function here
    
    # write any test case to test your function
    wheelOfFortune('e', 'test')
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
        def _wheel(self, letter, phrase):
            s = ''
            found = 0
            letter = letter.lower()
            phrase = phrase.lower()
            for c in phrase:
                if c == letter:
                    found = found + 1
                
            if found == 1:
                s = 'There was ' + str(found) + ' ' + letter + ' found\n'
            elif found > 1:
                s = 'There were ' + str(found) + ' ' + letter + "'s found\n"
            else:
                s = 'Sorry, there is no ' + '"' + letter + '"\n'
                  
            if found > 0:
                for i in range(len(phrase)):
                    if letter == phrase[i]:
                        s = s + 'Found at position ' + str(i) + '\n'
            return(s)
        
        def testOne(self):
            print('\nAuto-testing...')
            
            tests = [ ('z', 'The blue elephant ate a baloon',  "'z', 'The blue elephant ate a baloon'"),
                      ('T', 'The early bird catches the worm', "'t', 'The early bird catches the worm'"),
                      ('w', 'Work hard, play hard', "'w', 'Work hard, play hard'"),
                      ('A', 'Work hard, play hard', "'A', 'Work hard, play hard'") ]
                    
            for t in tests:
                s1 = t[0]
                s2 = t[1]
                c = t[2]
                
                oLen = len(self.getOutput())
                wheelOfFortune(s1, s2)
                oLenTest = len(self.getOutput())
                outText = self.getOutput()[oLen:oLenTest]  #extract new output           
    
                self.assertEqual(outText.strip(), self._wheel(s1, s2).strip(), c)
                
    
    myTests().main()