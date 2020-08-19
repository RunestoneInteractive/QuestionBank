.. activecode:: wvu_inheritance_car
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Inheritance
    :subchapter: Exercises
    :topics: Inheritance/Exercises
    :from_source: F

    Create a new class called **Car** that inherits from the existing **Vehicle** class. Add a class variable named **engine_size** to your new class with a value of ``None``.

    Create an instance of the new **Car** class to represent a car with the year, make, and model of your choice.

    Use your car's **print_vehicle()** method to print details about the car.

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