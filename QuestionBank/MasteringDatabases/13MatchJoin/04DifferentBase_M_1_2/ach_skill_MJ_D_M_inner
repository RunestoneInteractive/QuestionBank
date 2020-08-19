.. activecode:: ach_skill_MJ_D_M_inner
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 13MatchJoin
  :subchapter: 04DifferentBase_M_1_2
  :topics: 13MatchJoin/04DifferentBase_M_1_2
  :from_source: T
  :language: sql
  :include: all_creature_create

  -- same test town as origin town Achievement with its Skill data
              -- reduce by removing B.skillCode, B.origin_townId
  SELECT A.*, B.skillDescription,
              B.maxProficiency, B.minProficiency
  FROM achievement A
  INNER JOIN skill B       -- like MJ operator symbol
  ON A.skillCode = B.skillCode   -- equality match filters
  AND   A.test_townId = B.origin_townId
  ;