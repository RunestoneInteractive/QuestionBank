.. activecode:: cr1_cr2_times
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 16CompareJoin
   :subchapter: 01CompareJoin
   :topics: 16CompareJoin/01CompareJoin
   :from_source: T
   :language: sql
   :include: all_creature_create

   DROP TABLE IF EXISTS non_person_creature;
   CREATE TABLE non_person_creature AS
   SELECT * from creature
   WHERE creatureType != 'person';

   SELECT C1.creatureId C1_creatureId,
          C1.creatureName C1_creatureName,
          C1.reside_townId C1_reside_townId,
          C2.creatureId C2_creatureId,
          C2.creatureName C2_creatureName,
          C2.reside_townId C2_reside_townId
   FROM non_person_creature C1, non_person_creature C2
   ;