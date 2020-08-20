.. activecode::  str-ex-ducksq
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 06-strings
    :subchapter: 06-WriteCode
    :topics: 06-strings/06-WriteCode
    :from_source: T
    :nocodelens:

    In Robert McCloskey's book *Make Way for Ducklings*, the names of the ducklings are
    Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
    The following loop tries to output these names in order.
    Of course, that's not quite right because Ouack and Quack are misspelled.
    Can you fix it?
    ~~~~
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for p in prefixes:
        print(p + suffix)