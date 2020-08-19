.. activecode:: creature_ach_skill_oj
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 14OuterJoin
   :subchapter: 01OuterJoin
   :topics: 14OuterJoin/01OuterJoin
   :from_source: T
   :language: sql
   :include: all_creature_create

   -- This version is possible in SQLite, using
   -- only LEFT OUTER JOIN and UNION ALL
    SELECT C.creatureId,
        A.achId, A.skillCode, A.proficiency, A.test_townid
    FROM creature C LEFT JOIN achievement A
    ON C.creatureId=A.creatureId
    UNION ALL
    SELECT A.creatureId,
           A.achId, B.skillCode, A.proficiency, A.test_townId
    FROM  skill B LEFT JOIN achievement A
    ON A.skillCode = B.skillCode
    ;