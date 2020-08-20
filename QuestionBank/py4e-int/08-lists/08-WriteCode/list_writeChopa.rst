.. activecode:: list_writeChopa
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-WriteCode
    :topics: 08-lists/08-WriteCode
    :from_source: T
    :optional:

    def chop(lst):
        del lst[0]
        del lst[-1]
        return(lst)