.. parsonsprob:: mixedupcode_14_8
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

    Construct a class named "Dog"  that takes name and age as initial values and a class named "DogBreed"
    which takes in breed as an initial values and a function named "__str__" that returns teh string
    representation of the class.
    -----
    class Dog:
    =====
     def __init__(self, name, age):
    =====
      self.name = name
      self.age = age
    =====
    class DogBreed(Dog):
    =====
     def __init__(self, name ,age, breed):
    =====
      Dog.__init__(name, age)
    =====
      self.breed = breed
    =====
     def __str__(self):
    =====
      return ("Name: " + self.name  + " Age: " + self.age + " Breed:" + self.breed)
    =====
    lark = DogBreed("Lark", 10, "Golden Retriever")
    =====
    print("lark")