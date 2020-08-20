.. activecode:: stt
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Strings
    :subchapter: Loopingandcounting
    :topics: Strings/Loopingandcounting
    :from_source: None

    def count(text, aChar):
        lettercount = 0
        for c in text:
            if c == aChar:
                lettercount = lettercount + 1
        return lettercount

    print(count("banana","a"))
    print(count("banana","b"))