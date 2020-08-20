.. activecode:: survivor_times
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 15Divide
  :subchapter: 01Divide
  :topics: 15Divide/01Divide
  :from_source: T
  :language: sql
  :include: all_creature_create, survivor_input

  --------------------------------------------------------
  -- The times
  --

  drop table if exists achievingCr_survivorSkill_pair;
  drop table if exists achieving_creature;

  create table achieving_creature as
  SELECT distinct creatureId
  FROM crId_s_code_of_Achievement;

  create table achievingCr_survivorSkill_pair as
  SELECT achieving_creature.creatureId,
         skillCode_of_survivor_Skill.skillCode
  FROM skillCode_of_survivor_Skill,
       achieving_creature
  ;