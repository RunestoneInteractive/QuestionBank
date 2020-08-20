.. activecode:: str-ex-nameInputa
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-WriteCode
    :topics: 06-strings/06-WriteCode
    :from_source: T
    :optional:

    #CREATE PROMPT
    prompt = "What is your name?"
    #GET INPUT
    name = input(prompt)
    #ACCESS FIRST LETTER (INDEX 0)
    first = name[0]
    #MAKE LOWERCASE
    lowerFirst = lower(first)
    #PRINT
    print(lowerFirst)