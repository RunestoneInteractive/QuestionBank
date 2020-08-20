.. parsonsprob:: jk_xml_2
   :author: Jerry Kearns
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPTuring
   :subchapter: Exercises
   :topics: CSPTuring/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left

   Put the blocks into order to get all the countries and then loop through each country and print the name of that country and then get all the neighbors for that country and print the number of neighbors.   
   -----
       country_list = tree.findall("country")
   =====
       country_list = tree.find("country") #paired
   =====
       for country in country_list:
   =====
           print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxName: " + country.get("name"))
   =====
           neighbors = country.findall("neighbor")
   =====
           neighbors = country.find("neighbor") #paired 
   =====
           print("Num neighbors: %d" % len(neighbors))
   =====
           print("Num neighbors: %d" % neighbors) #paired