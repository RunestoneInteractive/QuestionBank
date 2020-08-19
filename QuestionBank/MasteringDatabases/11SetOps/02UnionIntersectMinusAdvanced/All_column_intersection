.. activecode:: All_column_intersection
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 11SetOps
   :subchapter: 02UnionIntersectMinusAdvanced
   :topics: 11SetOps/02UnionIntersectMinusAdvanced
   :from_source: T
   :language: sql
   :include: achievement_create_set2, aspiration_create_set2, AchievedSkillInTownWithProficiency

   SELECT creatureId, skillCode, proficiency, test_townId
   FROM AchievedSkillInTownWithProficiency
   INTERSECT
   SELECT creatureId, skillCode, aspiredProficiency, desired_townId
   FROM Aspiration;