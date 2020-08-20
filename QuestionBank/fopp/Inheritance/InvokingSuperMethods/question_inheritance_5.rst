.. mchoice:: question_inheritance_5
   :author: bmiller
   :difficulty: 3.1346153846
   :basecourse: fopp
   :chapter: Inheritance
   :subchapter: InvokingSuperMethods
   :topics: Inheritance/InvokingSuperMethods
   :from_source: T
   :answer_a: Error when invoked
   :answer_b: The string would not print out but d1 would have its hunger reduced.
   :answer_c: The string would print but d1 would not have its hunger reduced.
   :answer_d: Nothing would be different. It is the same as the current code.
   :feedback_a: Since we are no longer calling the parent method in the subclass method definition, the actions defined in the parent method feed will not happen, and only Arf! Thanks! will be printed.
   :feedback_b: Remember that the Python interpreter checks for the existence of feed in the Dog class and looks for feed in Pet only if it isn't found in Dog.
   :feedback_c: Since we are no longer calling the parent Pet class's method in the Dog subclass's method definition, the class definition will override the parent method.
   :feedback_d: Remember that the Python interpreter checks for the existence of feed in the Dog class and looks for feed in Pet only if it isn't found in Dog.
   :correct: c
   :pct_on_first: 0.4663461538
   :total_students_attempting: 208
   :num_students_correct: 206.0
   :mean_clicks_to_correct: 1.8737864078

   For the Dog class defined in the earlier activecode window, what would happen when d1.feed() is run if the Pet.feed(self) line was deleted?