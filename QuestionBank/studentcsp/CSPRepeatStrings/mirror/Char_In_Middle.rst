.. codelens:: Char_In_Middle
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatStrings
    :subchapter: mirror
    :topics: CSPRepeatStrings/mirror
    :from_source: T

    newString = "!"
    phrase = "We're off to see the Wizard!"
    for letter in phrase:
        newString = letter + newString + letter
    print(newString)