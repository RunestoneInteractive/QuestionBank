.. parsonsprob:: top-ten-Parsons
   :author: Barbara  Ericson
   :difficulty: 1.0
   :basecourse: StudentCSP
   :chapter: CSPNameNames
   :subchapter: Exercises
   :topics: CSPNameNames/Exercises
   :from_source: F
   :numbered: left
   :adaptive: 
   :pct_on_first: 0.0497925311
   :total_students_attempting: 241
   :num_students_correct: 236.0
   :mean_clicks_to_correct: 11.6398305085

   Put the code in order to create a function that prints the top 
   ten worst states for PM2.5 pollution. The function takes a list
   of dictionaries with the information for each state.  Each 
   dictionary contains the following keys: 'city', 'state', 'pm10', 
   'pm25'. It should create a new dictionary and loop through the 
   dictionaries in the passed list of dictionaries and then
   add the state as the key and the PM25 pollution as the value
   to the new dictionary. Then it should sort the list in 
   reverse order (highest to lowest).  Then it should print the 
   top ten state names and the PM25 pollution 
   for each state.
   -----
   def printTopTenWorstStatesPM25(dList):
   =====
       """ print the top ten worst states for pm 2.5 pollution
       dList -- the list of dictionaries that represents each line of the file
       """
   =====
       stateDict = {} 
   =====
       for dict in dList:
   =====
           state = dict["state"]
           poll25 = dict["pm25"]
   =====
           stateDict[state] = stateDict.get(state,0) + poll25
   =====
           stateDict[state] = stateDict.get(state,1) + poll25 #paired
   =====
       sortedList = sorted(stateDict.items(), key=lambda l: l[1], reverse = True)
   =====
       sortedList = sorted(stateDict.items(), key=lambda l: l[1]) #paired
   =====
       print("the 10 worst states for PM 2.5 pollution are:")
   =====
       for i in range(10):
   =====
       for i in range(11): #paired
   =====
           curr = sortedList[i]
   =====
           curr = sortedList[index] #paired
   =====
           print(curr[0] + " " + str(curr[1]))