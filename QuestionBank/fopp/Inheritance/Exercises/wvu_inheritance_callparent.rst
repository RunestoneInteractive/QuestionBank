.. activecode:: wvu_inheritance_callparent
    :author: Brian Powell
    :difficulty: 2.0
    :basecourse: fopp
    :chapter: Inheritance
    :subchapter: Exercises
    :topics: Inheritance/Exercises
    :from_source: F

    Copy and paste all the code from the `wvu_inheritance_override` question.

    Create a constructor (**__init__()**) function for the **Car** class. It should accept the year, make, model, and engine size as parameters. Have your function store the engine size, and then call the **Vehicle** class's constructor store the year, make, and model.

    Update your code to specify the engine size for your car using its constructor rather than setting it separately afterwards.

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