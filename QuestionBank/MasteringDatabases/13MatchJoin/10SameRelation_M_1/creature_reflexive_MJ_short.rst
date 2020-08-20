.. activecode:: creature_reflexive_MJ_short
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 13MatchJoin
   :subchapter: 10SameRelation_M_1
   :topics: 13MatchJoin/10SameRelation_M_1
   :from_source: T
   :language: sql
   :include: creature_create_MJ_reflexive

    SELECT C1.*,
           C2.creatureName AS idol_creatureName,
           C2.creatureType AS idol_creatureType,
           C2.reside_townId AS idol_reside_townId,
           C2.idol_creatureId AS idol_idol_creatureId
    FROM creature C1, creature C2
    WHERE C1.idol_creatureId = C2.creatureId;