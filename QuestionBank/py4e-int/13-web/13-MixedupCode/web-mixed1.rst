.. parsonsprob:: web-mixed1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 13-web
    :subchapter: 13-MixedupCode
    :topics: 13-web/13-MixedupCode
    :from_source: T
    :practice: T
    :numbered: left
    :adaptive:

    The following program converts a short bit of JSON data to Python. Drag the
    blocks of statements from the left column to the right column and put them in
    the right order. Watch out for an extra piece of code!
    -----
    import json
    =====
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    =====
    y = json.loads(x)
    =====
    y = json.dumps(x) #distractor
    =====
    print(y["age"])