.. mchoice:: pre_9
   :author: bmiller
   :difficulty: 3.0
   :basecourse: TeacherCSP
   :chapter: CSPrinTeasers
   :subchapter: pretest
   :topics: CSPrinTeasers/pretest
   :from_source: T
   :answer_a: The printed result will only contain vowels.
   :answer_b: The printed result will only contain consonants.
   :answer_c: It will print the empty string.
   :answer_d: The printed result will include "y"
   :answer_e: I don't know
   :correct: a
   :feedback_a: This only adds the letter if it is a vowel.
   :feedback_b: This only adds the letter if it is a vowel.
   :feedback_c: No, it will add vowels to newString and print that.
   :feedback_d: The letter must be in "aeiou" to be added to newString.
   :feedback_e: That is okay.  We do not expect you to know this.

   Given the following code segment, which of the statements below is true?

   ::

      newString = ""
      phrase = "Rubber baby buggy bumpers."
      for letter in phrase:
          if letter in "aeiou":
              newString = newString + letter
      print (newString)