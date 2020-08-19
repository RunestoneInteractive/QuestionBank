.. activecode:: word_counter2_130
   :author: Lloyd Smith
   :difficulty: 4.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :language: python3
   :nopair:

   Often, when dealing with text, we want to ignore certain words.
   For example, when searching for text we probably don't want to
   include words like a, the, of, and so forth. These words are
   called 'stopwords' and are usually kept in a file. Write a
   program to count the number of occurrences of words in some text
   but skip the stopwords. Again, use a dictionary to count the
   occurrences the display the words (in alphabetical order) and
   their counts. Use the text in the variable pp; the stopwords
   are stored in the variable stopwords. Note that the stopwords
   are separated by comma - not space.
   ~~~~
   import string

   pp = '''Peter Piper picked a peck of pickled peppers.
   A peck of pickled peppers Peter Piper picked.
   If Peter Piper picked a peck of pickled peppers
   Where's the peck of pickled peppers Peter Piper picked?'''

   stopwords = "a,an,any,can,if,is,it,it's,nor,not,of,on,nor,the"
   
   def remove_punc(s):
       '''Returns a copy of string s with all punctuation removed'''
       #This function is already written - don't change it!
       for char in string.punctuation:
           s = s.replace(char, '')
       return s

   def count_words(text, stopwords):
       '''Returns a dictionary with words and their counts'''
       #Create an empty dictionary
       #Split the text into a list of words
       #Split the stopwords into another list of words
       #For each word in the list
           #If the word is not in the stop list
               #If the word is not in the dictionary
                   #Add it with a count of 1
               #Otherwise
                   #Add 1 to the count
       #Return the dictionary

   def show_counts(word_dict):
       '''Display words and their counts'''
       #Get a list of the keys from word_dict
       #Put the words in alphabetical order
       #For each word in the list
           #Print the word and its count

   def main():
       '''Controls the program'''
       text = remove_punc(pp.lower())  #text is the name of the string with no punctuation
       #Use count_words to get a dictionary with words and counts; send it text and stopwords
       #Use show_counts() to display words and counts
   
   main()