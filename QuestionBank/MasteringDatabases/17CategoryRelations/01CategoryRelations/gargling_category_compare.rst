.. activecode:: gargling_category_compare
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 17CategoryRelations
  :subchapter: 01CategoryRelations
  :topics: 17CategoryRelations/01CategoryRelations
  :from_source: T
  :language: sql
  :include: all_creature_create, gargling_category

  SELECT distinct achievement.creatureId, gargling_category.category
  FROM achievement, gargling_category
  WHERE achievement.skillCode = gargling_category.skillCode
  AND   achievement.proficiency >= gargling_category.lowProfVal
  AND   achievement.proficiency <= gargling_category.highProfVal
  ;