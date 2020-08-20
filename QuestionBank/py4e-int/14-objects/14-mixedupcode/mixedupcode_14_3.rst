.. parsonsprob:: mixedupcode_14_3
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

    Construct a block of code that create a class named  'Cat'  that  takes 'name' and 'age' as initial value
    and returns cat info when 'info' is classed and returns meow when 'make_sound' function is called.
    -----
    class Cat:
    =====
     def __init__(self, name, age):
    =====
      self.name = name
      self.age = age
    =====
     def info(self):
    =====
      return(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    =====
     def make_sound(self):
    =====
      return("Meow")