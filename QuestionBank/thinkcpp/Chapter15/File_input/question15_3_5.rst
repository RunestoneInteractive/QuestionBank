.. parsonsprob:: question15_3_5
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter15
   :subchapter: File_input
   :topics: Chapter15/File_input
   :from_source: T
   :adaptive:
   :numbered: left

   Create a code block that reads lines from "filename" and prints them out. First, make sure that the file is able to be opened.
   -----
   int main () {
   =====
    string name_of_file = "filename";
   =====
    ifstream in_file (name_of_file.c_str());
   =====
    if (in_file.good() == false) {
   =====
      cout << "Unable to open the file named " << name_of_file;
   =====
      exit(1);
    }
   =====
    while (true) {
   =====
      getline(in_file, line);
   =====
      if (in_file.eof()) break;
   =====
      cout << line << endl;
    }
   }