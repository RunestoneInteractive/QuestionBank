.. activecode:: creature_ach_count
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 04Group
   :topics: 09UnaryOps/04Group
   :from_source: T
   :language: sql
   :include: achievement_create_group

   SELECT creatureId,
          count(distinct skillCode) AS achievedSkillCount
   FROM achievement
   GROUP BY creatureId;