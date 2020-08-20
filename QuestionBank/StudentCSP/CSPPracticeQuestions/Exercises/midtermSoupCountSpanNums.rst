.. parsonsprob:: midtermSoupCountSpanNums
   :author: Barbara  Ericson
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPPracticeQuestions
   :subchapter: Exercises
   :topics: CSPPracticeQuestions/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left
   :pct_on_first: 0.253968254
   :total_students_attempting: 126
   :num_students_correct: 116.0
   :mean_clicks_to_correct: 5.6637931034

   Put the mixed up code below in order to get all the span tags in a soup document and return the total of the numbers in the text of the span tags.
   -----
   def getSumSpanText(soup):
   =====
       total = 0
   =====
       tagList = soup.find_all('span')
   =====
       tagList = soup.find('span') #distractor
   =====
       for tag in tagList:
   =====
          total += int(tag.text)
   =====
       return total
   
   
   
   fig values (conf.py):
   
   arsons_div_class - custom CSS class of the component's outermost div