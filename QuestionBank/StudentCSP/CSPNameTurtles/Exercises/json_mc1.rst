.. mchoice:: json_mc1
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :answer_a: List, list, tuple
   :answer_b: List, string, dictionary
   :answer_c: String, list, dictionary
   :answer_d: String, list, tuple
   :correct: c
   :feedback_a: Triple quotes start a string in Python.
   :feedback_b: Triple quotes start a string in Python.
   :feedback_c: Data is a string, parsing the string returns a list, and the list is a list of dictionaries
   :feedback_d: What type of thing is in the data list?
   :pct_on_first: 0.6090225564
   :total_students_attempting: 133
   :num_students_correct: 133.0
   :mean_clicks_to_correct: 1.5488721805

   
   Which of the following are the correct types for data, info, and item? 
   
   .. code-block:: python 
   
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