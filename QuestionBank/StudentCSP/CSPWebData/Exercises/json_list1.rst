.. parsonsprob:: json_list1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.4488448845
   :total_students_attempting: 303
   :num_students_correct: 300.0
   :mean_clicks_to_correct: 3.63

   Put the blocks in order to import the libraries and then read JSON data from a file into a list of dictionaries.  If the length of the list is greater than 0 then loop through the  list of dictionaries and print the first name and email for each entry.  There are three extra blocks that are not needed in a correct solution.
   -----
   import json
   import os
   =====
   try:
       file = open('email.json', 'r') 
       contents = file.read()             
       dict_list = json.loads(contents)    
       file.close()    
   =====                     
   except:
       print("error when reading from file")
       dict_list = []
   =====
   if len(dict_list) > 0:
   =====
   if len(dict_list) == 0: #distractor
   =====
       for dict in dict_list:
   =====
           print("First: %s " % dict.get("first_name", None))
   =====
           print("First: %s " % dict[first_name] #distractor
   =====
           print("email: %s " % dict.get("email", None))
   =====
           print("email: %s " % dict[email] #distractor