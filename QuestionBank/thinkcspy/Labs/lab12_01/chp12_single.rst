.. activecode:: chp12_single
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Labs
    :subchapter: lab12_01
    :topics: Labs/lab12_01
    :from_source: T

    def countA(text):
        count = 0
        for c in text:
            if c == 'a':
                count = count + 1
        return count

    print(countA("banana"))