.. parsonsprob:: mixedupcode_14_7
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

    Construct a class named "Dog" that takes  name and age as initial values and a class named "GoldenRetriever"
    which contains a function named "__str__" that returns the string representation of the class.
    -----
    class Dog:
    =====
     def __init__(self, name, age):
    =====
      self.name = name
      self.age = age
    =====
    class GoldenRetriever extends Dog: #distractor
    =====
    class GoldenRetriever(Dog):
    =====
     def __str__(super): #distractor
    =====
     def __str__(self):
    =====
      return ("Name: " + super.name  + " Age: " + super.age + " Breed: "  + self.breed) #distractor
    =====
      return ("Name: " + self.name  + " Age: " + self.age + " Breed: Golden Retriever")
    =====
    lark = GoldenRetriever("Lark", 10)
    =====
    print(lark)