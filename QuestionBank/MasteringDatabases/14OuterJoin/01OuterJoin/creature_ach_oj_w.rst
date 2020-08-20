.. activecode:: creature_ach_oj_w
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 14OuterJoin
   :subchapter: 01OuterJoin
   :topics: 14OuterJoin/01OuterJoin
   :from_source: T
   :language: sql
   :include: all_creature_create

   DROP TABLE IF EXISTS CreatureLOJAchievement_w;

   CREATE TABLE CreatureLOJAchievement_w AS
   SELECT C.*, A.proficiency, A.skillCode, A.achDate
   FROM creature C
   LEFT OUTER JOIN achievement A
   ON
   (C.creatureId = A.creatureId and C.reside_townId = A.test_townId)
   ;
   -- creature is the left relation whose rows will be kept
   -- when the 'on' condition is not satisfied