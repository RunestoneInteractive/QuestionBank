.. activecode:: ch08_methods2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: StringMethods
    :topics: Strings/StringMethods
    :from_source: T


    food = "banana bread"
    print(food.capitalize())

    print("*" + food.center(25) + "*")
    print("*" + food.ljust(25) + "*")     # stars added to show bounds
    print("*" + food.rjust(25) + "*")

    print(food.find("e"))
    print(food.find("na"))
    print(food.find("b"))

    print(food.rfind("e"))
    print(food.rfind("na"))
    print(food.rfind("b"))

    print(food.index("e"))