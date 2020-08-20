.. activecode:: wvu_inheritance_override
    :author: Brian Powell
    :difficulty: 2.0
    :basecourse: fopp
    :chapter: Inheritance
    :subchapter: Exercises
    :topics: Inheritance/Exercises
    :from_source: F

    Copy and paste all the code from the `wvu_inheritance_car` question.

    In the **Car** class, override the **__str()__** class. The new version of the function should return the make, model, and year along with the engine size like "2015 Dodge Journey with 3.6L engine".

    For the car instance you created, set the **engine_size** property to the size of the car's engine.

    ~~~~
    class Vehicle:
        year = None
        make = None
        model = None

        def __init__(self, year, make, model):
            self.year = year
            self.make = make
            self.model = model

        def __str__(self):
            return "{} {} {}".format(self.year, self.make, self.model)

        def __repr__(self):
            return self.__str__()

        def print_vehicle(self):
            print(self.__str__())
    ====