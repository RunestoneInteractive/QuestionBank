.. parsonsprob:: web-mixed3
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

    The following program should parse some XML and extracts some data elements, but
    the code is mixed up. Drag the blocks of statements from the left column to the right column
    and put them in the right order. Watch out for indentation!
    -----
    import xml.etree.ElementTree as ET
    =====
    data = '''
    =====
    <person>
    ====
      <name>Chuck</name>
      <phone type="intl">
        +1 734 303 4456
    =====
      </phone>
    =====
      <email hide="yes" />
    =====
    </person>'''
    =====
    tree = ET.fromstring(data)
    =====
    print('Name:', tree.find('name').text)
    print('Attr:', tree.find('email').get('hide'))