.. activecode:: exactly_PK_debate
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 15Divide
   :subchapter: 01Divide
   :topics: 15Divide/01Divide
   :from_source: T
   :language: sql
   :include: all_creature_create

   DROP TABLE IF EXISTS PK_debate;
   -- 'the pattern' to look for
   CREATE TABLE PK_debate AS
   SELECT skillCode from skill
   WHERE skillCode = 'PK' or skillCode = "D3"
   ;

   -- Finish the code here for finding out who has achieved
   -- exactly penalty kick and debate.
   --
   DROP TABLE IF EXISTS creature_exactly_debate_pk;

   create table creature_exactly_debate_pk as
   -- fill here


   select * from creature_exactly_debate_pk;  -- leave this to display result