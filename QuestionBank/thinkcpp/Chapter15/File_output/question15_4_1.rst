.. parsonsprob:: question15_4_1
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter15
   :subchapter: File_output
   :topics: Chapter15/File_output
   :from_source: T
   :adaptive:
   :numbered: left

   Create a code block that sends output to a file. First, make sure that both the input file and the output file are able to be opened.
   -----
   int main () {
   =====
    ifstream in_file ("input_file_name");
    ofstream out_file ("input_file_name");
   =====
    if (in_file.good() == false || out_file.good() == false) {
   =====
      cout << "Unable to open one of the files." << endl;
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
      outfile << line << endl;
    }
   }