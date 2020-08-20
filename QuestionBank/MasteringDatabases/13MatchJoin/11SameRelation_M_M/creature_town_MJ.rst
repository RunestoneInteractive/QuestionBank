.. activecode:: creature_town_MJ
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 13MatchJoin
   :subchapter: 11SameRelation_M_M
   :topics: 13MatchJoin/11SameRelation_M_M
   :from_source: T
   :language: sql
   :include: creature_create_MJ_town

   SELECT C1.creatureId AS C1_creatureId,
          C1.creatureName AS C1_creatureName,
          C1.creatureType AS C1_creatureType,
          C1.reside_townId AS C1_reside_townId,
          C1.idol_creatureId AS C1_idol_creatureId,
          C2.creatureId AS C2_creatureId,
          C2.creatureName AS C2_creatureName,
          C2.creatureType AS C2_creatureType,
          C2.idol_creatureId AS C2_idol_creatureId
   FROM creature C1, creature C2
   WHERE C1.reside_townId = C2.reside_townId;