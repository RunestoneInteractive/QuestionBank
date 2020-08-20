.. parsonsprob:: mixedupcode_14_10
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

    Construct a class named "Apple" that contains type and color as initial value  and a function named "__repr__" that
    returns the string representation of the "Apple" class. Construct a class named "Farmer" that contains name as initial value
    with a function named updateItems that updates a list called 'items' which is a list of objects of Apple class and a function
    called "__str__" that returns the string representation of the class.
    -----
    class Apple:
    =====
     def __init__(self, type, color):
    =====
      self.type = type
      self.color = color
    =====
     def __repr__(self):
    =====
      return ("Apple type: " + self.type + " color: " + self.color)
    =====
    class Farmer:
    =====
     items = []
    =====
     def __init__(self, name):
      self.name = name
    =====
     def updateItems(self, type, color):
      items.append(Apple(type, color)
    =====
     def __str__(self):
      return("Farmer " + self.name + "has " + str(items)
    =====
    josh = Farmer("Josh")
    =====
    josh.updateItems("Granny Smith", "Green")
    print(josh)