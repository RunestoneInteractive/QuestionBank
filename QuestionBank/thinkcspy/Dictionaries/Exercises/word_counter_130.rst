.. activecode:: word_counter_130
   :author: Lloyd Smith
   :difficulty: 1.0
   :basecourse: thinkcspy
   :chapter: Dictionaries
   :subchapter: Exercises
   :topics: Dictionaries/Exercises
   :from_source: F
   :language: python3
   :nopair:

   Use a dictionary to count the number of occurrences of each word 
   in some text and display the words and their counts in alphabetical 
   order. Make the text lower case (already done for you). Do not
   display any word that does not occur in the text.
   ~~~~
   import string

   pp = '''Peter Piper picked a peck of pickled peppers.
   A peck of pickled peppers Peter Piper picked.
   If Peter Piper picked a peck of pickled peppers
   Where's the peck of pickled peppers Peter Piper picked?'''
   
   def remove_punc(s):
       '''Returns a copy of string s with all punctuation removed'''
       #This function is already written - don't change it!
       for char in string.punctuation:
           s = s.replace(char, '')
       return s

   def count_words(text):
       '''Returns a dictionary with words and their counts'''
       #Create an empty dictionary
       #Split the text into a list of words
       #For each word in the list
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
       #Use count_words to get a dictionary with words and counts
       #Use show_counts() to display words and counts
   
   main()