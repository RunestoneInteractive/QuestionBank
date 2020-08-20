.. activecode:: skill_count_per_town
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 10QueriesAfterUnary
   :subchapter: 00UnaryCombos
   :topics: 10QueriesAfterUnary/00UnaryCombos
   :from_source: T
   :language: sql
   :include: skill_create_group

   SELECT origin_townId,
          count(skillCode) AS SkillCount
   FROM Skill
   WHERE origin_townId is not null
   GROUP BY origin_townId;