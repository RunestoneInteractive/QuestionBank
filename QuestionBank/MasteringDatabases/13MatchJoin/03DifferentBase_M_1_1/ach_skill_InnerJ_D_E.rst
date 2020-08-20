.. activecode:: ach_skill_InnerJ_D_E
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 13MatchJoin
  :subchapter: 03DifferentBase_M_1_1
  :topics: 13MatchJoin/03DifferentBase_M_1_1
  :from_source: T
  :language: sql
  :include: all_creature_create

  -- Achievement with its Skill data
              -- reduce by removing B.skillCode
  SELECT A.*, B.skillDescription,
              B.maxProficiency, B.minProficiency,
              B.origin_townId
  FROM achievement A
  INNER JOIN skill B            -- like MJ operator symbol
  ON A.skillCode = B.skillCode   -- match filter over cols
  ;