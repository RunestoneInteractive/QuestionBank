.. activecode:: wvu_classes_str
    :author: Brian Powell
    :difficulty: 0.0
    :basecourse: fopp
    :chapter: Classes
    :subchapter: Exercises
    :topics: Classes/Exercises
    :from_source: F

    Add a **__str__()** function to the **Vehicle** class to return a string representation of object contents. Your function should return the vehicle's year, make, and model like "2015 Dodge Journey".

    Create an instance of the **Vehicle** class to represent a vehicle of your choice, and print your vehicle instance.
    ~~~~
    class Vehicle:
        def __init__(self, year, make, model):
            self.year = year
            self.make = make
            self.model = model
    ====