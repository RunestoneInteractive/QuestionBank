.. activecode:: tdj
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Dictionaries
    :subchapter: Dictionarymethods
    :topics: Dictionaries/Dictionarymethods
    :from_source: None

    inventory = {'bananas': 312, 'pears': 525, 'oranges': 217, 'apples': 430}

    for akey in inventory.keys():     # the order in which we get the keys is not defined
        print("Got key", akey, "which maps to value", inventory[akey])

    theKeys = list(inventory.keys())

    print(theKeys)