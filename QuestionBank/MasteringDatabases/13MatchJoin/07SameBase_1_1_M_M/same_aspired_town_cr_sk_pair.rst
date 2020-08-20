.. activecode:: same_aspired_town_cr_sk_pair
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 13MatchJoin
  :subchapter: 07SameBase_1_1_M_M
  :topics: 13MatchJoin/07SameBase_1_1_M_M
  :from_source: T
  :language: sql
  :include: all_creature_create

  DROP TABLE IF EXISTS sameTownCreatureSkillPair;

  -- same reside_townId as origin_townId Creature-Skill Pair
              -- reduce by removing B.townId
  CREATE TABLE sameTownCreatureSkillPair AS
  SELECT A.*, B.skillCode, B.skillDescription,
              B.maxProficiency, B.minProficiency
  FROM Creature A, Skill B       -- times
  WHERE A.reside_townId = B.origin_townId   -- equality match filter
  ;

  SELECT A.*, B.aspiredProficiency
  FROM sameTownCreatureSkillPair A, Aspiration B
  WHERE A.creatureId = B.creatureId
  AND   A. skillCode = B.skillCode
  AND A.reside_townId = B.desired_townId
  ;