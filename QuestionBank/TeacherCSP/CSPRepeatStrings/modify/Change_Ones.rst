.. codelens:: Change_Ones
    :author: bmiller
    :difficulty: 3.0
    :basecourse: TeacherCSP
    :chapter: CSPRepeatStrings
    :subchapter: modify
    :topics: CSPRepeatStrings/modify
    :from_source: T
    :question: What is the value of pos after the line with the red arrow executes?
    :breakline: 5
    :feedback: Remember that find returns the starting index if the target string is found and -1 if not.
    :correct: globals.pos

    str = "Th1s is a str1ng"
    pos = str.find("1")
    while pos >= 0:
        str = str[0:pos] + "i" + str[pos+1:len(str)]
        pos = str.find("1")
    print(str)