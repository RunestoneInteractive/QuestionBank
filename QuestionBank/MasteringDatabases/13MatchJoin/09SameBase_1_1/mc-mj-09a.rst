.. mchoice:: mc-mj-09a
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 13MatchJoin
   :subchapter: 09SameBase_1_1
   :topics: 13MatchJoin/09SameBase_1_1
   :from_source: T
   :answer_a: Aid(E), Bid(E)
   :answer_b: Aid(S), Bid(E)
   :answer_c: Aid(D), Bid(E)
   :answer_d: Aid(O), Bid(E)
   :correct: c
   :feedback_a: creatureId, skillCode is not exactly Achievement's identifier
   :feedback_b: creatureId, skillCode is not some of Achievement's identifier
   :feedback_c: Yes- creatureId, skillCode is disjoint from Achievement's identifier and exactly Aspiration's identifier.
   :feedback_d: creatureId, skillCode does not overlap with any of Achievement's identifier

   What would the 'works on' columns be in this case?