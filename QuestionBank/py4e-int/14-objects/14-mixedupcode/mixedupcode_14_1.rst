.. parsonsprob:: mixedupcode_14_1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 14-objects
    :subchapter: 14-mixedupcode
    :topics: 14-objects/14-mixedupcode
    :from_source: T
    :numbered: left
    :practice: T
    :adaptive:

    Construct a block of code that creates a class named Dog that takes 'name' as an initial value and
    returns it when 'getName' function is called.
    -----
    class Dog:
    =====
     name = ''
    =====
     def __init__(self, name):
    =====
      self.name = name
    =====
     def getName(self):
    =====
      return ("Dog name: " + self.name)