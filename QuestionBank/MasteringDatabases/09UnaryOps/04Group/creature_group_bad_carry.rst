.. activecode:: creature_group_bad_carry
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 04Group
   :topics: 09UnaryOps/04Group
   :from_source: T
   :language: sql
   :include: creature_create_group

   SELECT creatureType, reside_townId, count(creatureId)
   FROM creature
   GROUP BY creatureType;