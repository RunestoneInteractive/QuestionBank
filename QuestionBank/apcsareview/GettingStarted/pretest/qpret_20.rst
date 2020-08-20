.. mchoice:: qpret_20
    :author: bmiller
    :difficulty: 3.0
    :basecourse: apcsareview
    :chapter: GettingStarted
    :subchapter: pretest
    :topics: GettingStarted/pretest
    :from_source: T
    :answer_a: V.
    :answer_b: I and II
    :answer_c: I and III
    :answer_d: IV
    :answer_e: I only
    :correct: d
    :feedback_a: In fact, all of the reasons listed are valid. Subclasses can reuse methods written for superclasses without code replication, subclasses can be stored in the same array, and passed as arguments to methods meant for the superclass. All of which make writing code more streamlined.
    :feedback_b: III is also valid. In some cases you might want to store subclasses together in a single array, and inheritance allows for this.
    :feedback_c: II is also valid. In some cases a single method is applicable for a number of subclasses, and inheritance allows you to pass objects of the subclasses to the same method instead of writing individual methods for each subclass.
    :feedback_d: All of these are valid reasons to use an inheritance heirarchy.
    :feedback_e: II and III are also valid, in some cases a single method is applicable for a number of subclasses, and inheritance allows you to pass all the subclasses to the same method instead of writing individual methods for each subclass and you might want to store subclasses together in a single array, and inheritance allows for this.

    Which of the following reasons for using an inheritance heirarchy are valid?

    .. code-block:: java

        I.   Methods from a superclass can be used in a subclass without
             rewriting or copying code.
        II.  Objects from subclasses can be passed as arguments to a method
             designed for the superclass
        III. Objects from subclasses can be stored in the same array
        IV.  All of the above
        V.   None of the above