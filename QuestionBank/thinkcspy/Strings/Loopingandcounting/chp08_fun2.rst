.. activecode:: chp08_fun2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Loopingandcounting
    :topics: Strings/Loopingandcounting
    :from_source: T

    def count(text, aChar):
        lettercount = 0
        for c in text:
            if c == aChar:
                lettercount = lettercount + 1
        return lettercount

    print(count("banana","a"))