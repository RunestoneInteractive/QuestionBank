.. activecode:: hu_caesar_shift_prompt
    :author: Sean Joyce
    :difficulty: 4.0
    :basecourse: fopp
    :chapter: TransformingSequences
    :subchapter: Exercises
    :topics: TransformingSequences/Exercises
    :from_source: F
   
    Write a program that prompts the user to enter a string of text. Store the 
    text in variable ``plaintext``.  Your program should then prompt the user
    to enter a desired Caesar shift (this should be an integer in the range
    0 thru 25).  Store that value (after converting it to an integer) in a
    variable named ``shift``.  Your program should then encrypt 
    the user's original message, using the provided Caesar shift amount.
    Store the encrypted message in variable ``ciphertext``.  Print out the
    value of ``ciphertext`` as the last line in your program.
    ~~~~
    alphabet = "abcdefghijklmnopqrstuvwxyz"
 
    # assume the user enters only lowercase letters
    # they may also include spaces and punctuation 
    # in their original string; in those cases, 
    # those symbols should NOT be encrypted


    ====