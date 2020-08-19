.. activecode:: creature_ach_nj
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 14OuterJoin
   :subchapter: 01OuterJoin
   :topics: 14OuterJoin/01OuterJoin
   :from_source: T
   :language: sql
   :include: all_creature_create

   DROP TABLE IF EXISTS CreatureNJAchievement;

   CREATE TABLE CreatureNJAchievement AS
   SELECT C.*, A.proficiency, A.skillCode, A.achDate
   FROM creature C
   INNER JOIN achievement A
   ON C.creatureId = A.creatureId;

   SELECT * FROM CreatureNJAchievement
   ORDER BY creatureId;