.. activecode:: tdn
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Dictionaries
    :subchapter: Dictionarymethods
    :topics: Dictionaries/Dictionarymethods
    :from_source: None

    inventory = {'bananas': 312, 'pears': 525, 'oranges': 217, 'apples': 430}

    print(inventory.get("apples"))
    print(inventory.get("cherries"))

    print(inventory.get("cherries", 0))