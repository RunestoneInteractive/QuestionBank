.. activecode:: survivor
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 15Divide
   :subchapter: 01Divide
   :topics: 15Divide/01Divide
   :from_source: T
   :language: sql
   :include: all_creature_create

   drop table if exists skillCode_of_survivor_Skill;

   -- This is our pattern relation B
   --
   CREATE TABLE skillCode_of_survivor_Skill AS
   SELECT skillCode from skill
   WHERE skillDescription = 'float' OR skillDescription = 'swim'
   ;

   -- This is the Divide operation using available SQL,
   -- including two 'nested' queries.
   --
   SELECT DISTINCT creatureId
   FROM achievement AS IN1
   WHERE NOT EXISTS
       (SELECT *
          FROM skillCode_of_survivor_Skill P
         WHERE NOT EXISTS
               (SELECT *
                  FROM achievement AS IN2
                 WHERE (IN1.creatureId = IN2.creatureId)
                   AND (IN2.skillCode = P.skillCode)));