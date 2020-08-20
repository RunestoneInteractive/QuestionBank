.. mchoice:: question_inheritance_4
   :author: bmiller
   :difficulty: 2.6186046512
   :basecourse: fopp
   :chapter: Inheritance
   :subchapter: InvokingSuperMethods
   :topics: Inheritance/InvokingSuperMethods
   :from_source: T
   :answer_a: 5
   :answer_b: ["Mrrp"]
   :answer_c: ["chirp"]
   :answer_d: Error
   :feedback_a: This would print if the code was print(b1.chirp_number).
   :feedback_b: We set b1 to be Bird('tweety', 5) above.  Bird is a subclass of Pet, which has ["Mrrp"] for sounds, but Bird has a different value for that class variable. The interpreter looks in the subclass first.
   :feedback_c: The interpeter finds the value in the class variable for the class Bird.
   :feedback_d: We ran set b1 to be Bird('tweety', 5) above.  Bird has a value set for the attribute sounds.
   :correct: c
   :pct_on_first: 0.5953488372
   :total_students_attempting: 215
   :num_students_correct: 213.0
   :mean_clicks_to_correct: 1.5774647887

   What will print when ``print(b1.sounds)`` is run?