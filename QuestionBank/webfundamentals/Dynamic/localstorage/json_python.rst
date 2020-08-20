.. activecode:: json_python
    :author: bmiller
    :difficulty: 3.0
    :basecourse: webfundamentals
    :chapter: Dynamic
    :subchapter: localstorage
    :topics: Dynamic/localstorage
    :from_source: T

    import json

    print(json.dumps({'foo': 1, 'bar':2}))
    x = json.dumps([1,2,3,4])
    print("x is a ", type(x))
    print(x)

    y = json.loads(x)
    print("y is a ", type(y))
    y.append(5)
    print(y)