.. activecode:: stw
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Strings
    :subchapter: StringMethods
    :topics: Strings/StringMethods
    :from_source: None

    ss = "    Hello, World    "

    els = ss.count("l")
    print(els)

    print("***" + ss.strip() + "***")
    print("***" + ss.lstrip() + "***")
    print("***" + ss.rstrip() + "***")

    news = ss.replace("l", "***")
    print(news)