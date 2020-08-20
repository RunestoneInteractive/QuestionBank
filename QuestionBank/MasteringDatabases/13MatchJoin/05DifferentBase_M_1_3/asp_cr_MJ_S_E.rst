.. activecode:: asp_cr_MJ_S_E
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 13MatchJoin
  :subchapter: 05DifferentBase_M_1_3
  :topics: 13MatchJoin/05DifferentBase_M_1_3
  :from_source: T
  :language: sql
  :include: all_creature_create

  -- Aspiration with its Creature data
              -- reduce by removing B.creatureId
  SELECT A.*, B.creatureName, B.creatureType,
              B.reside_townId, B.idol_creatureId
  FROM Aspiration A, Creature B       -- times
  WHERE A.creatureId = B.creatureId   -- equality match filter
  ;