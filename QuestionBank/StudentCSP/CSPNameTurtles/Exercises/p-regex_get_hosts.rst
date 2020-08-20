.. parsonsprob:: p-regex_get_hosts
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameTurtles
   :subchapter: Exercises
   :topics: CSPNameTurtles/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.235042735
   :total_students_attempting: 234
   :num_students_correct: 233.0
   :mean_clicks_to_correct: 4.8712446352

   The code below is correct, but is mixed-up.  It is passed a list of lines from a file.  It returns a list of the unique hostnames which are in the format "@alphanum.alphanum.alphanum" with at least one alphanumeric character after the '@' and after each '.'
   -----
   def find_hosts(lines):
   =====
       host_list = []
   =====
       for line in lines:
   =====
           line = line.rstrip() # get rid of end of line
   =====
           found_list = re.findall(r"@(\w+\.\w+\.\w+)",line)
   =====
           found_list = re.search(r"@(\w+\.\w+\.\w+)",line) #distractor
   =====
           for item in found_list:
   =====
               if item not in host_list:
   =====
                   host_list.append(item)
   =====
       return host_list