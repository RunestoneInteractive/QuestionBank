.. activecode:: liu
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Lists
    :subchapter: PureFunctions
    :topics: Lists/PureFunctions
    :from_source: None

    def doubleStuff(a_list):
        """ Return a new list in which contains doubles of the elements in a_list. """
        new_list = []
        for value in a_list:
            new_elem = 2 * value
            new_list.append(new_elem)
        return new_list

    things = [2, 5, 9]
    print(things)
    stuff = doubleStuff(things)
    print('things', things)
    print('stuff', stuff)