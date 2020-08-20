.. activecode:: creature_join_town
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 03TwoEntityShapes
   :subchapter: TwoEntityShapes
   :topics: 03TwoEntityShapes/TwoEntityShapes
   :from_source: T
   :language: sql
   :include: town_create, town_populate, creature_create_2, creature_populate_2

   SELECT creatureName, townName
   FROM creature natural join town;