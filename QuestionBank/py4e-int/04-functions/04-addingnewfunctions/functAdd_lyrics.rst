.. activecode:: functAdd_lyrics
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-addingnewfunctions
    :topics: 04-functions/04-addingnewfunctions
    :from_source: T
    :coach:
    :caption: This example demonstrates that the value of print_lyrics is a function object, which has type "function".

    def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')

    print(print_lyrics)
    print(type(print_lyrics))