.. activecode:: answer10_8_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Dictionaries
    :subchapter: Exercises
    :topics: Dictionaries/Exercises
    :from_source: F

    x = input("Enter a sentence")

    x = x.lower()   # convert to all lowercase

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    letter_count = {} # empty dictionary
    for char in x:
        if char in alphabet: # ignore any punctuation, numbers, etc
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1

    keys = letter_count.keys()
    for char in sorted(keys):
        print(char, letter_count[char])