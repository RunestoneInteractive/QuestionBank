.. activecode:: 1306_prac3_rev2
    :author: Shishir Shah
    :difficulty: 0.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: Exercises
    :topics: Strings/Exercises
    :from_source: F
    :language: python


    Write a function ``count_hi(str, caseSensitive)`` which **returns** a count of the number of times
    ``hi`` appears anywhere in the given string. ``caseSensitive`` is a Boolean where when
    True does a case sensitive comparison, but if False, will be case insensitive.

    You may **NOT** use the ``.count`` method. 

    ::

      count_hi('abc hi ho', True)  returns a 1
      count_hi('ABCHi hi', False)  returns a 2

    ~~~~
    def count_hi(str, caseSensitive):
        # Write your code here

    ====