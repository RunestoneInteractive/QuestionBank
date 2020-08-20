.. activecode:: chp12_dict10
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Dictionarymethods
    :topics: Dictionaries/Dictionarymethods
    :from_source: T

    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

    print(inventory.get("apples"))
    print(inventory.get("cherries"))

    print(inventory.get("cherries", 0))