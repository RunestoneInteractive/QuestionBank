.. activecode:: relay4x100_ButNot_gargling_achieveing_creature
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 11SetOps
  :subchapter: 01UnionIntersectMinusSimple
  :topics: 11SetOps/01UnionIntersectMinusSimple
  :from_source: T
  :language: sql
  :include: achievement_create_set, 4x100relay_creature, gargling_creature

  DROP TABLE IF EXISTS Relay4x100ButNotgarglingCreature;

  CREATE TABLE Relay4x100ButNotgarglingCreature AS
  SELECT creatureId
  FROM relay4x100Creature
  EXCEPT
  SELECT creatureId
  FROM garglingCreature;

  SELECT * FROM Relay4x100ButNotgarglingCreature;