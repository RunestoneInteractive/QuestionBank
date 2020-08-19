.. activecode:: ach_aspired_cr_sk_pair
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 13MatchJoin
  :subchapter: 09SameBase_1_1
  :topics: 13MatchJoin/09SameBase_1_1
  :from_source: T
  :language: sql
  :include: all_creature_create

  DROP TABLE IF EXISTS achievingCreatureSkillPair;

  -- achieving Creature-Skill Pair
  CREATE TABLE achievingCreatureSkillPair AS
  SELECT distinct creatureId, skillCode
  FROM Achievement
  ;

  SELECT A.*, B.aspiredProficiency,
              B.desired_townId
  FROM achievingCreatureSkillPair A, Aspiration B
  WHERE A.creatureId = B.creatureId
  AND   A. skillCode = B.skillCode
  ;