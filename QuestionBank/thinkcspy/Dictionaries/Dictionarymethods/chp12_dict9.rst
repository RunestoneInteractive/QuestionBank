.. activecode:: chp12_dict9
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Dictionaries
    :subchapter: Dictionarymethods
    :topics: Dictionaries/Dictionarymethods
    :from_source: T

    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
    print('apples' in inventory)
    print('cherries' in inventory)

    if 'bananas' in inventory:
        print(inventory['bananas'])
    else:
        print("We have no bananas")