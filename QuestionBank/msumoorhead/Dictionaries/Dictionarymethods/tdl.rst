.. activecode:: tdl
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Dictionaries
    :subchapter: Dictionarymethods
    :topics: Dictionaries/Dictionarymethods
    :from_source: None

    inventory = {'bananas': 312, 'pears': 525, 'oranges': 217, 'apples': 430}

    print(list(inventory.values()))
    print(list(inventory.items()))

    for k in inventory:
        print("Got", k, "that maps to", inventory[k])

    for (k,v) in inventory.items():
        print(k, "maps to", v)