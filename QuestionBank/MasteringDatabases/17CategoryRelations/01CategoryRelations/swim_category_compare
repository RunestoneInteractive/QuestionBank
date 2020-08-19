.. activecode:: swim_category_compare
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 17CategoryRelations
   :subchapter: 01CategoryRelations
   :topics: 17CategoryRelations/01CategoryRelations
   :from_source: T
   :language: sql
   :include: all_creature_create, swim_category

   SELECT distinct achievement.creatureId, swim_category.category
   FROM achievement, swim_category
   WHERE achievement.skillCode = swim_category.skillCode
   AND   achievement.proficiency >= swim_category.lowProfVal
   AND   achievement.proficiency <= swim_category.highProfVal
   ;