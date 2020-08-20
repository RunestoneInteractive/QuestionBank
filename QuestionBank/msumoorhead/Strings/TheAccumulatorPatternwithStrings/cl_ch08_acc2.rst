.. codelens:: cl_ch08_acc2
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Strings
    :subchapter: TheAccumulatorPatternwithStrings
    :topics: Strings/TheAccumulatorPatternwithStrings
    :from_source: None

    def removeVowels(s):
        vowels = "aeiouAEIOU"
        newString = ""
        for aChar in s:
            if aChar not in vowels:
                newString = newString + aChar
        return newString

    print(removeVowels("compsci"))