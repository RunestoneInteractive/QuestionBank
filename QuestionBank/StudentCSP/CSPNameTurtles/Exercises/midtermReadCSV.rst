.. parsonsprob:: midtermReadCSV
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.12
   :total_students_attempting: 125
   :num_students_correct: 125.0
   :mean_clicks_to_correct: 5.184

   Put the mixed up code below in order to define a function user_counts that reads from a csv file and returns a dictionary of the users and the number of times each user has an entry in the log file.
   -----
   def user_counts(filename):
   =====
       dir = os.path.dirname(__file__)
       userDict = dict()
   =====
       with open(os.path.join(dir, filename)) as csv_file:
   =====
           csv_reader = csv.reader(csv_file)
   =====
           csv_reader = Reader(csv_file) #distractor
   =====
           for cols in csv_reader:
   =====
           for line in lines: #distractor
   =====
               user = cols[3]
   =====
               user = cols.get(3) #distractor
   =====
               userDict[user] = userDict.get(user,0) + 1
   =====
               userDict[user] = userDict[user] + 1 #distractor
   =====
       return userDict