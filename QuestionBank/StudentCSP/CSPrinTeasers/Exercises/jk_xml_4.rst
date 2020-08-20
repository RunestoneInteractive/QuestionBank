.. parsonsprob:: jk_xml_4
   :author: Jerry Kearns
   :difficulty: 0.0
   :basecourse: StudentCSP
   :chapter: CSPrinTeasers
   :subchapter: Exercises
   :topics: CSPrinTeasers/Exercises
   :from_source: F
   :adaptive: 
   :numbered: left

   This is just a problem from a teacher practicing writing Parsons Problem    
   -----
       country_list = tree.findall("country")
   =====
       country_list = tree.find("country") #paired
   =====
       for country in country_list:
   =====
           print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxName: " + country.get("name"))
   =====
           neighbors = country.findall("neighbor")
   =====
           neighbors = country.find("neighbor") #paired 
   =====
           print("Num neighbors: %d" % len(neighbors))
   =====
           print("Num neighbors: %d" % neighbors) #paired