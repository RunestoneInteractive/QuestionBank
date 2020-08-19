.. codelens:: strParsing
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-parsing
    :topics: 06-strings/06-parsing
    :from_source: T
    :question: What is the value of sppos after the line with the red arrow executes?
    :breakline: 4
    :feedback: The second argument in find() is the start position.
    :correct: globals.sppos

    data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
    atpos = data.find('@')
    print(atpos)
    sppos = data.find(' ',atpos)
    print(sppos)
    host = data[atpos+1:sppos]
    print(host)