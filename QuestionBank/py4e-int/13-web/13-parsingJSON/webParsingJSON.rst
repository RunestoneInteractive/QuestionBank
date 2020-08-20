.. activecode:: webParsingJSON
    :author: bmiller
    :difficulty: 3.0
    :basecourse: py4e-int
    :chapter: 13-web
    :subchapter: 13-parsingJSON
    :topics: 13-web/13-parsingJSON
    :from_source: T
    :caption: Parsing JSON

    import json

    data = '''
    [
      { "id" : "001",
       "x" : "2",
       "name" : "Chuck"
      } ,
      { "id" : "009",
       "x" : "7",
       "name" : "Brent"
      }
    ]'''

    info = json.loads(data)
    print('User count:', len(info))

    for item in info:
        print('Name', item['name'])
        print('Id', item['id'])
        print('Attribute', item['x'])