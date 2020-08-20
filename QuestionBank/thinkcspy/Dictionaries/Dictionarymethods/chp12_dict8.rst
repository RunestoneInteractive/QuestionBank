.. activecode:: chp12_dict8
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Dictionarymethods
    :topics: Dictionaries/Dictionarymethods
    :from_source: T

    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

    print(list(inventory.values()))
    print(list(inventory.items()))

    for (k,v) in inventory.items():
        print("Got", k, "that maps to", v)

    for k in inventory:
        print("Got", k, "that maps to", inventory[k])