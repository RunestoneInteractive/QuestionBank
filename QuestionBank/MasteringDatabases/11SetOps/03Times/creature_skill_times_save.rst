.. activecode:: creature_skill_times_save
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 11SetOps
   :subchapter: 03Times
   :topics: 11SetOps/03Times
   :from_source: T
   :language: sql
   :include: creature_skill_create_times

   DROP TABLE IF EXISTS Creature_Skill_Pair;

   CREATE TABLE Creature_Skill_Pair AS
   SELECT creature.*, skill.*
   FROM creature, skill;