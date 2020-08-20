.. activecode:: london_person_creature
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 01Filter
   :topics: 09UnaryOps/01Filter
   :from_source: T
   :language: sql
   :include: creature_create_filter

   SELECT *
   FROM creature
   WHERE creatureType = 'person' AND reside_townId = 'le';