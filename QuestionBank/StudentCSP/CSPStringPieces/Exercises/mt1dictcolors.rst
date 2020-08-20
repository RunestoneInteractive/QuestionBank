.. parsonsprob:: mt1dictcolors
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPStringPieces
   :subchapter: Exercises
   :topics: CSPStringPieces/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.4770318021
   :total_students_attempting: 283
   :num_students_correct: 282.0
   :mean_clicks_to_correct: 1.9219858156

   Put the blocks in order to define the function get_color_counts to take a list of colors as strings and 
   return a dictionary that has the number of times each unique color appears in the list.
   -----
   def get_color_counts(color_list):
   =====
   def get_color_counts(self, color_list): #paired
   =====
       color_dict = dict()
   =====
       color_dict = new dict() #paired
   =====
       for color in color_list:
   =====
           color_dict[color] = color_dict.get(color,0) + 1
   =====
           color_dict[color] = color_dict[color] + 1 #paired
   =====
       return color_dict