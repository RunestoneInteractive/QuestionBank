.. activecode:: creature_count_skills_ge_2
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 10QueriesAfterUnary
   :subchapter: 00UnaryCombos
   :topics: 10QueriesAfterUnary/00UnaryCombos
   :from_source: T
   :language: sql
   :include: achievement_create_filter

   DROP TABLE IF EXISTS creatureAchievedSkillCount;

   CREATE TABLE creatureAchievedSkillCount AS
   SELECT creatureId,
          count(distinct skillCode) AS achievedSkillCount
   FROM achievement
   GROUP BY creatureId;

   SELECT *
   FROM creatureAchievedSkillCount
   WHERE achievedSkillCount >= 2;