.. activecode::  strstuff
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Introduction
    :subchapter: InputandOutput
    :topics: Introduction/InputandOutput
    :from_source: T
    :caption: The input Function Returns a String

    aName = input("Please enter your name ")
    print("Your name in all capitals is",aName.upper(),
          "and has length", len(aName))