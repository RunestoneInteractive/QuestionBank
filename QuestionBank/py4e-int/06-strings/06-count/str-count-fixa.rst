.. activecode:: str-count-fixa
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-count
    :topics: 06-strings/06-count
    :from_source: T
    :nocodelens:

    def count(text, aChar):
        lettercount = 0
        for c in text:
            if c == aChar:
                lettercount = lettercount + 1
    return lettercount