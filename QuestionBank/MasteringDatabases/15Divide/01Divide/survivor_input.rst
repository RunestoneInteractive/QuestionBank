.. activecode:: survivor_input
  :author: bmiller
  :difficulty: 3.0
  :basecourse: MasteringDatabases
  :chapter: 15Divide
  :subchapter: 01Divide
  :topics: 15Divide/01Divide
  :from_source: T
  :language: sql
  :include: all_creature_create

  -- First create the PATTERN relation (B) of survivor skill
  drop table if exists skillCode_of_survivor_Skill;

  CREATE TABLE skillCode_of_survivor_Skill AS
  SELECT skillCode from skill
  WHERE skillDescription = 'float' OR skillDescription = 'swim'
  ;

  --------------------------------------------------------
  -- Reduce to creatureId, skillCode columns of achievement
  -- (relation A)
  --
  drop table if exists crId_s_code_of_Achievement;

  CREATE TABLE crId_s_code_of_Achievement AS
  select distinct creatureId, skillCode
  from achievement
  ;