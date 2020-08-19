.. parsonsprob:: json_pp2
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNumbers
   :subchapter: Exercises
   :topics: CSPNameNumbers/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.1842105263
   :total_students_attempting: 114
   :num_students_correct: 114.0
   :mean_clicks_to_correct: 8.3684210526

   Put the following in order to create a function get_data to try and get the sunrise and sunset data for a location.  If it fails print an error. If it succeeds print the data. 
   -----
   def get_data(lat, long):
   =====
       try:
   =====
           parms = str(lat) + "&lng=" + str(long) +"&date=today"
   =====
           url = "https://api.sunrise-sunset.org/json?lat=" + parms
   =====
           r = requests.get(url)
   =====
           dict = json.loads(r.text) 
   =====        
       except:
   =====
           print("error when reading from url")
           dict = {}
   =====
       if len(dict) > 0:
   =====
           answer_dict = dict.get("results", None)
   =====
           print("Sunrise is at: " + answer_dict.get("sunrise", None))
           print("Sunset is at: " + answer_dict.get("sunset", None))