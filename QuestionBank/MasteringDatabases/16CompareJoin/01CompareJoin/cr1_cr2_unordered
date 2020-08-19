.. activecode:: cr1_cr2_unordered
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 16CompareJoin
   :subchapter: 01CompareJoin
   :topics: 16CompareJoin/01CompareJoin
   :from_source: T
   :language: sql
   :include: all_creature_create

   SELECT C1.creatureId C1_creatureId,
          C1.creatureName C1_creatureName,
          C1.reside_townId C1_reside_townId,
          C2.creatureId C2_creatureId,
          C2.creatureName C2_creatureName,
          C2.reside_townId C2_reside_townId
   FROM creature C1, creature C2
   WHERE C1_reside_townId = C2_reside_townId
   AND C1_creatureId < C2_creatureId   -- this is the 'compare'
   ;