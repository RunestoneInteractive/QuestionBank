.. parsonsprob:: listMixed_weather
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 08-lists
    :subchapter: 08-MixedupCode
    :topics: 08-lists/08-MixedupCode
    :from_source: T
    :practice: T
    :adaptive:
    :numbered: left

    Write a program that will print out the length of each item in the list as well as
    the first and last characters of the item. Watch out for extra code blocks and indentation!
    -----
    weather = ["sunny", "cloudy", "partially sunny", "rainy", "storming", "windy", "foggy", "snowy", "hailing"]
    =====
    for condition in weather:
    =====
        print("The word is", len(condition), "characters")
    =====
        first_char = condition[0]
        last_char = condition[-1]
    =====
        print("The first character is: " + first_char)
        print("The last character is: " + last_char)