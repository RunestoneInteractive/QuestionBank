.. activecode:: r5_ex6 
    :author: Irma Ravkic
    :difficulty: 1.0
    :basecourse: fopp
    :chapter: Sequences
    :subchapter: Exercises
    :topics: Sequences/Exercises
    :from_source: F
   
    Let us create a simple funny nickname generator. We will refine it in the future when we learn more tools. To do that, randomly generate the first name from the adjectives list,  and the last name from the noun list given below in the code. Before you inform the user of the generated nickname, make sure you capitalize both the first and the last name (use the appropriate function, do not hard  code!). The user should see something like this: Your nickname is: Squishy Panda.  Make sure you use indexing and the random number generator. Every time you run your  finalized code, something else should be printed, without you changing anything in your code! Do not hard code! You cannot write: print('Your nickname is', 'Squishy', 'Panda') 

    ~~~~
    adjectives = ['fabulous', 'squishy', 'evil', 'fuzzy', 'smooth', 'nosy', 'bitter', 'salty', 'mammoth', 'sweet', 'grumpy', 'modern', 'shivering', 'melted']
    nouns = ['elephant', 'phone', 'bug', 'string', 'nose', 'finger', 'tongue', 'laptop', 'koala', 'panda', 'mouse']
    ====