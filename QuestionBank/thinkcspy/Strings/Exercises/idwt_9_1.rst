.. activecode:: idwt_9_1
    :author: Meg Blume-Kohout
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python
    :autograde: unittest

    Write a function ``capTitle(line)`` that capitalizes the first letter of each word in the line
    as in a title header of a newspaper. The first word is always capitalized. Special words are
    not capitalized - such as 'a', 'the', etc.

    A list ``specialWords`` is in the code below which contains all the special words that are **not**
    to be capitalized (unless it is the first word of the title).

    The function should **return** a string of the capitalized line.

    Example titles:

    ::

      The Story of the Amazing Rat
      A Battle That Will Never Be Forgotten
      In the Beginning of Time

    ~~~~
    import string
    
    # the list of special words - you can use this as a global variable
    # within your function
    specialWords = ['a', 'an', 'the', 'at', 'by', 'for', 'in', 
                   'of', 'on', 'to', 'up', 'and', 'as', 
                   'but', 'or', 'nor']
    
    # define the capTitle() function here
    
    # some test cases
    print(capTitle("the story of the amazing rat"))
    
    ====
    from unittest.gui import TestCaseGui
    
    class myTests(TestCaseGui):
    
        def _next(self, line):
            # extract 1st word assuming first ch is letter
            done = False
            i = 0
            word = line[i]
            while not done:
                i = i + 1
                if i < len(line):
                    if line[i] not in string.whitespace:
                        word = word + line[i]
                    else:
                        done = True
                else:
                    # no more letters in line
                    done = True
                
            for w in specialWords:
                if word.lower() == w:
                    return(True)
            return(False)
            
        def _title(self, line):
            firstWordFound = False
            inWord = False
            o = ''
            for i in range(len(line)):
                if line[i] in string.whitespace:
                    # print whitespace and mark the end of word
                    o = o + line[i]
                    inWord = False
                else:
                    # handle a letter
                    if not firstWordFound:
                        # first letter of first word capitalize
                        o = o + line[i].upper()
                        firstWordFound = True
                        inWord = True
                    elif inWord:
                        # in the middle of a word
                        o = o + line[i]
                    else:
                        # first letter of new word
                        inWord = True
                        if not self._next(line[i:]):
                            o = o + line[i].upper()
                        else:
                            o = o + line[i].lower()
        
            return (o)
    
        def testOne(self):
            print('\nAuto-testing...')
            
            tests = [ 'the cat In The hat',
                      "a day in mary's and joe's life in the year 1999",
                      'how to think like a CS person and write code']
                    
            for t in tests:
                self.assertEqual(capTitle(t), self._title(t), t)
                
    
    myTests().main()