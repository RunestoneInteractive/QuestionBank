.. parsonsprob:: exp1_q5_pp
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.4842105263
   :total_students_attempting: 95
   :num_students_correct: 92.0
   :mean_clicks_to_correct: 2.5543478261

   Put the blocks in order to define the function get_names that takes a list of dictionaries and returns a list of strings with the names from the dictionaries. The key for the first name is ‘first’ and the key for the last name is ‘last’. Return a list of the full names (first last) as a string. If the ‘first’ or ‘last’ key is missing in the dictionary use ‘Unknown’.
   -----
   def get_names(list_of_dict):
   =====
    name_list = []
   =====
    for p_dict in list_of_dict:
   =====
        first = p_dict.get('first', 'Unknown')
        last = p_dict.get('last', 'Unknown')
   =====
        first = p_dict.get('first', None)
        last = p_dict.get('last',  None) #distractor
   =====
        name = first + " " + last
   =====
        name = first + last #distractor
   =====
        name_list.append(name)
   =====
    return name_list