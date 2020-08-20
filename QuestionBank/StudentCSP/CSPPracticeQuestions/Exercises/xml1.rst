.. parsonsprob:: xml1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.4657039711
   :total_students_attempting: 277
   :num_students_correct: 271.0
   :mean_clicks_to_correct: 2.184501845

   Put the blocks in order to import the needed module, define the data, read an XML tree from the data, and print the name and email hide attribute value.
   -----
   import xml.etree.ElementTree as ET
   =====
   data = '''
        &#60;person&#62;
           &#60;name&#62;Chuck&#60;/name&#62;
           &#60;phone type="intl"&#62;
              +1 734 303 4456
           &#60;/phone&#62;
           &#60;email hide="yes" /&#62;
       &#60;/person&#62;'''
   =====
   tree = ET.fromstring(data)
   =====
   print('Name:', tree.find('name').text)
   =====
   print('Attr:', tree.find('email').get('hide'))