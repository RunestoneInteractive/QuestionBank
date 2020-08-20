.. activecode:: creature_ach_oj_count
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 14OuterJoin
  :subchapter: 01OuterJoin
  :topics: 14OuterJoin/01OuterJoin
  :from_source: T
  :language: sql
  :include: all_creature_create, creature_ach_oj

  SELECT creatureId, count(skillCode)
  FROM CreatureLOJAchievement
  GROUP BY creatureId;