.. activecode:: ch08_methods1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: Strings
    :subchapter: StringMethods
    :topics: Strings/StringMethods
    :from_source: T

    ss = "    Hello, World    "

    els = ss.count("l")
    print(els)

    print("***" + ss.strip() + "***")
    print("***" + ss.lstrip() + "***")
    print("***" + ss.rstrip() + "***")

    news = ss.replace("o", "***")
    print(news)