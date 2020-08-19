.. activecode:: after_set_intermediate
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 12QueryAfterSet
   :subchapter: 00TimesFilterReduceEx
   :topics: 12QueryAfterSet/00TimesFilterReduceEx
   :from_source: T
   :language: sql
   :include: achievement_create_project
   :enabledownload:

   -- top left side of chart
   DROP TABLE IF EXISTS AchievedSkillWithProficiency;
   CREATE TABLE AchievedSkillWithProficiency AS
   SELECT distinct creatureId, skillCode, proficiency
   FROM achievement;

   -- top right side of chart
   DROP TABLE IF EXISTS MaxProficiencyAchievedPerSkill;
   CREATE TABLE MaxProficiencyAchievedPerSkill AS
   SELECT skillCode, max(proficiency) AS maxProficiency
   FROM achievement
   GROUP BY skillCode;

   -- Times (duplicate skillCode renamed)
   DROP TABLE IF EXISTS AchievedSkill_MaxProficiency_Pair;
   CREATE TABLE AchievedSkill_MaxProficiency_Pair AS
   SELECT A.*, B.skillCode AS maxSkillCode, B.maxProficiency
   FROM AchievedSkillWithProficiency A,
        MaxProficiencyAchievedPerSkill B;

   -- Filter, reduce and compute proficiencyDifference
   DROP TABLE IF EXISTS AchSkillByCreatureDifferenceFromMax;
   CREATE TABLE AchSkillByCreatureDifferenceFromMax AS
   SELECT creatureId, skillCode,
           maxProficiency - proficiency AS proficiencyDifference
   FROM AchievedSkill_MaxProficiency_Pair
   WHERE skillCode = maxSkillCode;