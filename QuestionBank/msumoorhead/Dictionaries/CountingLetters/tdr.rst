.. activecode:: tdr
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Dictionaries
    :subchapter: CountingLetters
    :topics: Dictionaries/CountingLetters
    :from_source: None

    def countA(text):
        count = 0
        for c in text:
            if c == 'a':
                count = count + 1
        return count

    print(countA("banana"))