.. mchoice:: JP_AP2-2-4
   :author: John Pataracchia
   :difficulty: 0.0
   :basecourse: csawesome
   :chapter: Unit2-Using-Objects
   :subchapter: practice-test-objects
   :topics: Unit2-Using-Objects/practice-test-objects
   :from_source: F
   :answer_a: ChemicalElement elem = new ChemicalElement(14.0074);
   :answer_b: new ChemicalElement elem = 14.0074;
   :answer_c: ChemicalElement elem = new ChemicalElement();
   :answer_d: ChemicalElement elem = 14.0074;
   :answer_e: ChemicalElement elem = ChemicalElement(14.0074);
   :correct: a
   :feedback_a: Correct
   :feedback_b: new is incorrectly placed.
   :feedback_c: This creates an object but it does not set its atomic mass to 14.0074.
   :feedback_d: The call to the constructor is missing.
   :feedback_e: The keyword new is missing.
   :pct_on_first: 0.4864864865
   :total_students_attempting: 37
   :num_students_correct: 36.0
   :mean_clicks_to_correct: 2.1666666667

    Consider the following class. Which of the following code segments, when placed in a method in a class other than ChemicalElement, will construct a ChemicalElement object elem with an atomic mass of 14.0074?
   
    .. code-block:: java
   
        public class ChemicalElement
        {
            private double atomicMass;
            private int atomicNumber;
   
            public ChemicalElement()
            {
                atomicMass = 0.0;
            }
   
            public ChemicalElement(double b)
            {
                atomicMass = b;
            }
        }