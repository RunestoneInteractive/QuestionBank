.. activecode:: CCS_padding_one
   :author: Michael McCarrin
   :difficulty: 0.0
   :basecourse: thinkcspy
   :chapter: Debugging
   :subchapter: Exercises
   :topics: Debugging/Exercises
   :from_source: F

   'Padding' is a term for adding characters to  a set of strings so they all have the same width. For example, if my strings are"I", "In", "Ink", "Inkling" and I want them to all have a length of 8, I can accomplish this by padding them on the left with the "*" character. The result would be:
   
   ::

     "*******I"
     "******In"
     "*****Ink"
     "*Inkling"
    
   I could also pad them on the right side. In that case I would get:
   
   ::
   
   "I*******"
   "In******"
   "Ink*****"
   "Inkling*" 
     
   **Write a program that does the following:**

   #. Ask the user to enter a word that is 8 letters or fewer.
   #. Pad it to 9 characters on the left with the "#" character and print the result.
   #. Next, pad the original word to 9 characters on the RIGHT with the "%" character and print the result.
   
   **NOTE: The IF statement is not permitted.**
   ~~~~