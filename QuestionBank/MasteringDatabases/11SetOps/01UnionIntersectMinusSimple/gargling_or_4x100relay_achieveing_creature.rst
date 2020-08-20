.. activecode:: gargling_or_4x100relay_achieveing_creature
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 11SetOps
   :subchapter: 01UnionIntersectMinusSimple
   :topics: 11SetOps/01UnionIntersectMinusSimple
   :from_source: T
   :language: sql
   :include: achievement_create_set, 4x100relay_creature, gargling_creature

   DROP TABLE IF EXISTS garglingOr4x100RelayCreature;

   CREATE TABLE garglingOr4x100RelayCreature AS
   SELECT creatureId
   FROM garglingCreature
   UNION
   SELECT creatureId
   FROM relay4x100Creature;

   SELECT * FROM garglingOr4x100RelayCreature;