.. activecode:: cr1_cr2_times_3
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
   WHERE creatureType != 'person'
   ;

   SELECT C1.creatureId C1_creatureId,
          C2.creatureId C2_creatureId
   FROM non_person_creature C1, non_person_creature C2
   -- add WHERE clause here
   ;