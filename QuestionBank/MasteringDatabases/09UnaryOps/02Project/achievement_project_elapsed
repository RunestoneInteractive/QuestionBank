.. activecode:: achievement_project_elapsed
   :author: bmiller
   :difficulty: 3.0
   :basecourse: MasteringDatabases
   :chapter: 09UnaryOps
   :subchapter: 02Project
   :topics: 09UnaryOps/02Project
   :from_source: T
   :language: sql
   :include: achievement_create_project

   SELECT achId, skillCode, proficiency,
          julianday('now') - julianday(achDate) AS
            totalElapsedTimeSinceAchieved
   FROM achievement;