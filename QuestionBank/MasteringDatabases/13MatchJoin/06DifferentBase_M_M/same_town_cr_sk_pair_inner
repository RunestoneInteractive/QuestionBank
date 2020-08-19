.. activecode:: same_town_cr_sk_pair_inner
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 13MatchJoin
  :subchapter: 06DifferentBase_M_M
  :topics: 13MatchJoin/06DifferentBase_M_M
  :from_source: T
  :language: sql
  :include: all_creature_create

  -- same reside_townId as origin_townId Creature-Skill Pair
              -- reduce by removing B.townId
  SELECT A.*, B.skillCode, B.skillDescription,
              B.maxProficiency, B.minProficiency
  FROM Creature A
  INNER JOIN Skill B       -- like MJ operator symbol
  ON A.reside_townId = B.origin_townId   -- equality match filter
  ;