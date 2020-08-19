.. parsonsprob:: question15_5_4
   :author: bmiller
   :difficulty: 3.0
   :basecourse: thinkcpp
   :chapter: Chapter15
   :subchapter: Parsing_input
   :topics: Chapter15/Parsing_input
   :from_source: T
   :adaptive:
   :numbered: left

   Create a block of code that takes a date written in the format "mm/dd/yyyyy"
   as an argument, and that separates it into three separate integers: day,
   month, and year. Find the respective parts in this order: month, first slash,
   day, second slash, year.
   -----
   int main () {
   =====
    string month = date.substr(0, 2);
   =====
    string month = date.substr(2, 0);                              #paired
   =====
    int first_slash = date.find('/');
   =====
    string day = date.substr(first_slash + 1, 2);
   =====
    string day = date.substr(first_slash, 2);                              #paired
   =====
    int second_slash = date.find('/', first_slash + 1);
   =====
    int second_slash = date.find('/', first_slash);                              #paired
   =====
    int second_slash = date.find('/');                              #paired
   =====
    string year = date.substr(second_slash + 1, 4);
   =====
    string year = date.substr(second_slash, 4);                              #paired
   =====
    string year = date.substr(second_slash + 1, 2);                              #paired
   =====
   }