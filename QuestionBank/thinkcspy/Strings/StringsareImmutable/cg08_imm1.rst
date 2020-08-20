.. activecode:: cg08_imm1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: StringsareImmutable
    :topics: Strings/StringsareImmutable
    :from_source: T

    greeting = "Hello, world!"
    greeting[0] = 'J'            # ERROR!
    print(greeting)