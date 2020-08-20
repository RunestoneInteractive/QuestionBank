.. activecode:: creature_skill_times
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 11SetOps
   :subchapter: 03Times
   :topics: 11SetOps/03Times
   :from_source: T
   :language: sql
   :include: creature_skill_create_times

   SELECT creature.*, skill.*
   FROM creature, skill;