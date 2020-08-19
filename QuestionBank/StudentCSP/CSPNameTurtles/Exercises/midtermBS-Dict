.. parsonsprob:: midtermBS-Dict
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.4032258065
   :total_students_attempting: 124
   :num_students_correct: 124.0
   :mean_clicks_to_correct: 2.7580645161

   Put the code in order to define a function that takes a soup object and a target class name and returns a dictionary for the links with the target class.  The dictionary keys are the link text and the values are the urls.
   -----
   def get_dict(soup, target_class):
   =====
       linkDict = {}
   =====
       links = soup.find_all('a', class_=target_class)
   =====
       links = soup.find_all('a', class=target_class) #distractor
   =====
       for link in links:
   =====
           linkDict[link.text] = link.get('href', None)
   =====
           linkDict[link.text] = link['href'] #distractor
   =====
       return linkDict