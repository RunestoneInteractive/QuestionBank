.. activecode:: survivor_at_least
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 15Divide
  :subchapter: 01Divide
  :topics: 15Divide/01Divide
  :from_source: T
  :language: sql
  :include: all_creature_create, survivor_input, survivor_times, survivor_missing

  --------------------------------------------------------
  -- The second minus at the bottom of the chart
  --
  drop table if exists creatureId_of_survivor_Creature;

  --  Using except, it would be like this
  --
  -- CREATE TABLE creatureId_of_survivor_Creature AS
  -- SELECT distinct creatureId
  -- FROM crId_s_code_of_Achievement
  -- EXCEPT
  -- SELECT distinct creatureId
  -- FROM creatureId_skillCode_missing_cr_sur_skill
  -- ;

  -- using NOT EXISTS, such as in MySQL, it would look like this
  --
  CREATE TABLE creatureId_of_survivor_Creature AS
  SELECT distinct creatureId
  FROM crId_s_code_of_Achievement IN1
  WHERE NOT EXISTS
    (SELECT creatureId
     FROM creatureId_skillCode_missing_cr_sur_skill MISSING
     WHERE IN1.creatureId = MISSING.creatureId
     )
  ;

  select * from creatureId_of_survivor_Creature;