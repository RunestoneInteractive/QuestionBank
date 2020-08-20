.. activecode:: functDef_lyrics
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 04-functions
    :subchapter: 04-definitionsanduses
    :topics: 04-functions/04-definitionsanduses
    :from_source: T
    :coach:
    :caption: An example of a user-defined function being called within another user-defined function.

    def print_lyrics():
        print("I'm a lumberjack, and I'm okay.")
        print('I sleep all night and I work all day.')

    def repeat_lyrics():
        print_lyrics()
        print_lyrics()

    repeat_lyrics()