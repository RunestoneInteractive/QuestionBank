.. activecode:: CCS_splitting_decimals
   :author: Michael McCarrin
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Debugging
   :subchapter: Exercises
   :topics: Debugging/Exercises
   :from_source: F
   
   **Complete the program below. It should do the following:**
      
   #. Ask the user to entry a value between 0 and 100.
   #. Store the value as a float.
   #. Print the part of the value that is to the left of the decimal.
   #. Print the part of the value that is to the right of the decimal.
   #. Print an equation that adds the two parts together to get the total value.
   
   **NOTE: For this exercise, it is OK to print the floating point approximation of the decimal part of the user's entry, rather than the exact original entry.**
   ~~~~
   entry_str   = input("Please enter a decimal value between 0 and 100:")

   entry_float = float(entry_str)

   left_side   = 0 #FIXME
   right_side  = 0 #FIXME

   print("The part of your entry to the left of the decimal point is:", left_side)

   print("The part of your entry to the right of the decimal point is approximately:", right_side)

   print(entry_str, "=", left_side, "+", right_side)