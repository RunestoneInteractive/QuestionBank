.. activecode::  strstuff
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Introduction
    :subchapter: InputandOutput
    :topics: Introduction/InputandOutput
    :from_source: T
    :caption: The input Function Returns a String

    a_name = input("Please enter your name ")
    print("Your name in all capitals is",a_name.upper(),
          "and has length", len(a_name))