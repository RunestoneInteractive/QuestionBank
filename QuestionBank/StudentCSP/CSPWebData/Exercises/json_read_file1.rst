.. parsonsprob:: json_read_file1
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPWebData
   :subchapter: Exercises
   :topics: CSPWebData/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1871165644
   :total_students_attempting: 326
   :num_students_correct: 322.0
   :mean_clicks_to_correct: 6.3043478261

   Put the blocks in order to import the needed packages.  Then try to read JSON from a file into a dictionary.  Set total to 0 and if that dictionary has at least one item in it, then get a list (of dictionaries) from that dictionary using the key "comments".  Then loop through the dictionaries in that list and add the value of the "count" key (if it exists) to total.  Print the total. There are two extra blocks that are not needed in a correct solution.
   -----
   import json
   import os
   =====
   try:
       file = open('comments_42.json', 'r') 
       contents = file.read()              
       dict = json.loads(contents)         
       file.close()                         
   =====
   except:
       print("error when reading from file")
       dict = {}
   =====
   total = 0
   if len(dict) > 0:
   =====
   if dict:     #distractor
   =====
       personDictList = dict.get("comments", None)
   =====
       for personDict in personDictList:
   =====
           total = total +  personDict.get("count",0)
   =====
           total = total +  personDict[count] #distractor
   =====
   print(total)