.. activecode:: creature_skill_MJ
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 13MatchJoin
   :subchapter: 01Circumstances
   :topics: 13MatchJoin/01Circumstances
   :from_source: T
   :language: sql
   :include: creature_skill_create_times_MJ

   SELECT creature.*, S.skillCode, S.skillDescription,
          S.maxProficiency, S.minProficiency
   FROM creature, skill S
   WHERE reside_townId = origin_townId
   ;