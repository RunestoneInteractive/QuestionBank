.. mchoice:: question9_2_1
   :author: bmiller
   :difficulty: 4.0773638968
   :basecourse: fopp
   :chapter: Files
   :subchapter: FindingaFileonyourDisk
   :topics: Files/FindingaFileonyourDisk
   :from_source: T
   :answer_a: open("YearlyProjections.csv", "r")
   :answer_b: open("../CompanyData/YearlyProjections.csv", "r")
   :answer_c: open("CompanyData/YearlyProjections.csv", "r")
   :answer_d: open("Project/CompanyData/YearlyProjections.csv", "r")
   :answer_e: open("../YearlyProjections.csv", "r")
   :correct: c
   :feedback_a: This would try to open a file inside of Project (but that is not where the file is.)
   :feedback_b: This would go to the parent directory of Project and look for a subdirectory of that called CompanyData. But CompanyData is inside Project so it wouldn't be found.
   :feedback_c: Yes, this is how you can access the file!
   :feedback_d: This would try to find a subdirectory Project of the current directory called Project.
   :feedback_e: Remember that '..' will bring you up one level to the parent directory. This would try to open a csv file in the parent directory of Project (but that is not where the file is.)
   :practice: T
   :pct_on_first: 0.2306590258
   :total_students_attempting: 1396
   :num_students_correct: 1380.0
   :mean_clicks_to_correct: 2.7528985507

   Say you are in a directory called Project. In it, you have a file with your Python code. You would like to read in data from a file called "YearlyProjections.csv" which is in a folder called CompanyData, which is inside of Project. What is the best way to open the file in your Python program?