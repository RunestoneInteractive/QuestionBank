.. activecode:: THR_Skill
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 15Divide
   :subchapter: 01Divide
   :topics: 15Divide/01Divide
   :from_source: T
   :language: sql
   :include: all_creature_create

   drop table if exists ThreeLeggedRaceSkill;
   -- 'the pattern' to look for
   CREATE TABLE ThreeLeggedRaceSkill AS
   SELECT skillCode from skill
   WHERE skillCode = 'THR'
   ;