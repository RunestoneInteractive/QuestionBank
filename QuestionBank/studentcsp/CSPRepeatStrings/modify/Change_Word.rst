.. codelens:: Change_Word
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPRepeatStrings
    :subchapter: modify
    :topics: CSPRepeatStrings/modify
    :from_source: T
    :question: What is the value of pos after the line with the red arrow executes?
    :breakline: 6
    :feedback: Remember that find returns the starting index if the target string is found and -1 if not.
    :correct: globals.pos

    str = "He wanted a peice of candy"
    str = str + " so he gave her a peice."
    pos = str.find("peice")
    while pos >= 0:
        str = str[0:pos] + "piece" + str[pos+len("peice"):len(str)]
        pos = str.find("peice")
    print(str)