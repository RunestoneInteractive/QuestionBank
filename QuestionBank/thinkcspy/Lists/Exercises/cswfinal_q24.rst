.. parsonsprob:: cswfinal_q24
   :author: Lloyd Smith
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Lists
   :subchapter: Exercises
   :topics: Lists/Exercises
   :from_source: F
   :pct_on_first: 0.2820512821
   :total_students_attempting: 39
   :num_students_correct: 35.0
   :mean_clicks_to_correct: 3.9428571429

   24. Assume the file cities.csv holds the populations of a number of cities in Missouri, one on each line, in the form city_name, county_name, population. For example, the entry for Sprinfield would read Springfield, Greene, 167319. Put the following lines of code in the correct order to create a function that returns the total population of all the cities.
   -----
   def population(lines):
   '''Returns the total population of cities in the file'''
   =====
       total = 0
   =====
       for row in lines:
   =====
           data = row.strip().split(',')
   =====
           total += int(data[2])
   =====
       return total