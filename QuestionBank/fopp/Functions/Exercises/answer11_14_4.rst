.. activecode:: answer11_14_4
    :author: bmiller
    :difficulty: 3.0
    :basecourse: fopp
    :chapter: Functions
    :subchapter: Exercises
    :topics: Functions/Exercises
    :from_source: T
    :nocodelens:

    def reverse(mystr):
        reversed = ''
        for char in mystr:
            reversed = char + reversed
        return reversed

    def mirror(mystr):
        return mystr + reverse(mystr)

    assert mirror('good') == 'gooddoog'
    assert mirror('Python') == 'PythonnohtyP'
    assert mirror('') == ''
    assert mirror('a') == 'aa'