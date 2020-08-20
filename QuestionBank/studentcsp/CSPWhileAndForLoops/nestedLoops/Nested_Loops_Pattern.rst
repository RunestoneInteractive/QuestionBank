.. activecode:: Nested_Loops_Pattern
    :author: bmiller
    :difficulty: 3.0
    :basecourse: studentcsp
    :chapter: CSPWhileAndForLoops
    :subchapter: nestedLoops
    :topics: CSPWhileAndForLoops/nestedLoops
    :from_source: T

    for x in range(0,2):
        line = ""
        for y in range(0,3):
            line = line + '*'
        print(line)