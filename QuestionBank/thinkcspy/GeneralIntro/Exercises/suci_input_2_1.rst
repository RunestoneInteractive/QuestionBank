.. actex:: suci_input_2_1
   :author: peter suci
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: GeneralIntro
   :subchapter: Exercises
   :topics: GeneralIntro/Exercises
   :from_source: F

   Run the program then add lines to the program so that it not only prints the first name, but also asks for the last name and then prints the last name.

   ~~~~
   dash_header_width = int(input("enter dash header width"))
   first_name = input("enter first name")
   print(dash_header_width * "-")
   print("You entered",first_name,"as your first name")