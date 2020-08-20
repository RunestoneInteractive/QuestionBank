.. activecode:: str_q11_answer
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: T
    :nocodelens:

    from test import testEqual

    def remove(substr,theStr):
        index = theStr.find(substr)
        if index < 0: # substr doesn't exist in theStr
            return theStr
        return_str = theStr[:index] + theStr[index+len(substr):]
        return return_str

    testEqual(remove('an', 'banana'), 'bana')
    testEqual(remove('cyc', 'bicycle'), 'bile')
    testEqual(remove('iss', 'Mississippi'), 'Missippi')
    testEqual(remove('egg', 'bicycle'), 'bicycle')