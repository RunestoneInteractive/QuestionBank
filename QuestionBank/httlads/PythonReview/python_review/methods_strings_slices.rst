.. activecode:: methods_strings_slices
   :author: bmiller
   :difficulty: 3.0
   :basecourse: httlads
   :chapter: PythonReview
   :subchapter: python_review
   :topics: PythonReview/python_review
   :from_source: T
   :coach:

   my_var = "Abc defg hij"
   print(len(my_var))
   print(my_var[2:6])
   print(my_var * 2)

   print(my_var.lower())
   print(my_var.upper())
   print(my_var.startswith("Abc"))
   print(my_var.endswith("xyz"))
   print(my_var.title())
   list_of_string = my_var.split(" ")
   new_string = "-".join(list_of_string)
   print(new_string)