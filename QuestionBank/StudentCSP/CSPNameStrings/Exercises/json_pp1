.. parsonsprob:: json_pp1
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameStrings
   :subchapter: Exercises
   :topics: CSPNameStrings/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1391304348
   :total_students_attempting: 115
   :num_students_correct: 115.0
   :mean_clicks_to_correct: 4.8869565217

   Put the following in order to read JSON data from a file into a variable called data.  Close the file right after you read the data from it.
   -----
   import json
   =====
   source_dir = os.path.dirname(__file__)
   full_path = os.path.join(source_dir, 'comments_42.json')
   file = open(full_path, 'r') # Try to read the data from the file
   =====
   contents = file.read() 
   =====
   contents = file.readlines() #paired
   =====
   file.close() 
   =====
   data = json.loads(string)
   =====
   data = json.dumps(string) #paired