.. activecode:: active0py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: AlgorithmAnalysis
    :subchapter: AnAnagramDetectionExample
    :topics: AlgorithmAnalysis/AnAnagramDetectionExample
    :from_source: T
    :caption: Checking Off Python
    :optional:

    #checks to see if the anagrams have the same number of characters

    def anagramSolution1(s1,s2):
        stillOK = True
        if len(s1) != len(s2):
            stillOK = False
            return stillOK

        lists2 = list(s2)
        pos1 = 0

        # checks to see if all of the letters are the same in both inputs
        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            while pos2 < len(lists2) and not found:
                if s1[pos1] == lists2[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1

            if found:
                lists2[pos2] = None
            else:
                stillOK = False

            pos1 = pos1 + 1

        return stillOK

    def main():
        print(anagramSolution1('abcd','dcba'))
    main()