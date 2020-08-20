.. activecode:: msdie_initial1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: ProperClasses
    :subchapter: a_proper_python_class
    :topics: ProperClasses/a_proper_python_class
    :from_source: T
    :language: python

    import random

    class MSDie:
        """
        Multi-sided die

        Instance Variables:
            current_value
            num_sides

        """

        def __init__(self, num_sides):
            self.num_sides = num_sides
            self.current_value = self.roll()

        def roll(self):
            self.current_value = random.randrange(1,self.num_sides+1)
            return self.current_value

        def __str__(self):
            return str(self.current_value)

        def __repr__(self):
            return "MSDie({}) : {}".format(self.num_sides, self.current_value)


    my_die = MSDie(6)
    for i in range(5):
        print(my_die)
        my_die.roll()

    d_list = [MSDie(6), MSDie(20)]
    print(d_list)