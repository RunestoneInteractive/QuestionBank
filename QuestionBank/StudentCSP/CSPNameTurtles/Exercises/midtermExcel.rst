.. parsonsprob:: midtermExcel
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.52
   :total_students_attempting: 125
   :num_students_correct: 125.0
   :mean_clicks_to_correct: 2.656

   Put the mixed up code below in order to define a function get_results that gets the number of students who passed the AP exam with a 3 (row 72), 4 (row 71), or 5 (row 70) and the percent that passed for a column from an excel spreadsheet.  Return a tuple with the total who passed and the percentage that passed.
   -----
   def get_results(infile, col):
   =====
   define get_results(infile, col): #distractor
   =====
       wb = load_workbook(infile)
       ci = column_index_from_string(col)
   =====
       ws = wb['All']
   =====
       num_fives = ws.cell(row = 70, column = ci).value
       num_fours = ws.cell(row = 71, column = ci).value
       num_threes = ws.cell(row = 72, column = ci).value
   =====
       total_pass = num_fives + num_fours + num_threes
       total = ws.cell(row = 75, column = ci).value
   =====
       percent_pass = total_pass / total * 100
   =====
       return (total_pass, percent_pass)
   =====
       return [total_pass, percent_pass] #distractor