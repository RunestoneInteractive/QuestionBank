.. activecode:: bmhsProj1
    :author: victor truong
    :difficulty: 1.0
    :basecourse: thinkcspy
    :chapter: SimplePythonData
    :subchapter: Exercises
    :topics: SimplePythonData/Exercises
    :from_source: F
    :language: python

    Following the instructions in the comments
    ~~~~
    '''Mad Lib   
    **Remember to comment EVERY LINE of code and include the 
    output as a multi line comment and the top of your code before 
    submitting **
    
    Python can be used for a variety of different tasks. In this project, 
    we'll use Python to write a Mad Libs story! Mad Libs are stories with 
    blank spaces that a reader can fill in with their own words. The 
    result is usually a funny (or strange) story. 
    
    Mad Libs require:
    · Words from the reader (for the blank spaces) 
    · A story to plug the words into 
    
    For this project, we'll provide you with the story (feel free to modify 
    it), but it will be up to you to build a program that does the following: 
      1. Prompt the user for input 
      2. Print the entire Mad Libs story with the user's input in the right 
    places 

    Let's begin! 

     1. It's helpful to let other developers know what your program does. 
    Begin by including a multi-line comment that starts on line 3 that 
    describes what your program does. 
    
    Hint
     """ This program does
     the following... 
     Author: your-name """ 
    
    2. Let's first inform the user that the program is running. Print a 
    message to let the user know that Mab Libs has started.
   
    Hint
     print ("Mad Libs is starting!")

    3. The story that we have provided you with is going to need a main 
    character. Ask the user to input a name, then store the user's input 
    in a variable. Note: It's common practice to use short, but 
    descriptive variable names. 
    
    Hint
     name = input("Enter a name: ") 
    
     4. For our story, you will need to ask the user for three adjectives. 
    Similar to Step 3, ask the user for input three separate times. Store 
    each adjective that the user inputs into descriptive variables. 
    
    Hint
     first_adj = input("Enter an adjective: ") 

    second_adj = input("Enter a second adjective: ") 

    third_adj = input("Enter one more adjective: ") 

    5. You'll also need to ask the user for three verbs. Just like in Step 
    4, ask the user for input three separate times. Store each verb in 
    descriptive variables. 

    Hint
     first_verb = input("Enter a verb: ") 
     #Prompt for the second verb here 
     #And the third verb here
 
    6. We're also going to need some nouns in our story. This time, ask 
    the user to input four nouns. Store each noun into its own 
    descriptive variable.

    Hint
     first_noun = input("Enter a noun: ") 
     #Don't forget the other three nouns 

    7. This is where the story can get really fun (and weird)! Ask the 
    user to input one of each of the following: 
    · An animal 
    · A food 
    · A fruit 
    · A number 
    · A superhero name 
    · A country 
    · A dessert 
    · A year 
 
    Make sure to save the input into variables.

    Hint
     animal = input("Enter an animal: ") 
     #Don't forget to prompt for the rest of the items! 
 
    8. At this point, we have all the words needed for the Mad Libs 
    story. The next step is to insert all of the user's inputs into the blank 
    spaces of the story. Take a look at the variable named STORY. It is 
    set equal to a string that contains our story template.

    9. Use string formatting to insert the user's inputs into the story. We 
    already formatted some of the STORY string for you with %s, but 
    it's up to you to finish the rest of the string formatting anywhere you 
    see _. 

    Hint
     Note: The snippet of code below has been abbreviated.
    STORY = "This morning I woke up and felt %s because %s was 
    going to finally %s over the big %s %s. On the other side of the %s 
    were..."
    
    10. Now it's time to tell your tale! The final line of code should print 
    the story and insert the inputs into the right blanks. The user's 
    inputs should be inserted in the following order (get ready!):
     1. First adjective
     2. Name 
     3. First verb 
     4. Second adjective 
     5. First noun 
     6. Second noun 
     7. Animal 
     8. Food 
     9. Second verb 
     10. Third noun 
     11. Fruit 
     12. Third adjective 
     13. Name 
     14. Third verb 
     15. Number 
     16. Name 
     17. Superhero name 
     18. Superhero name
     19. Name 
     20. Country 
     21. Name 
     22. Dessert 
     23. Name 
     24. Year 
     25. Fourth noun 
 
    Hint
     Using the variable names from the hints in Steps 4, 5, 6:
     print (STORY % (first_adj, name, first_verb, ..., fourth_noun))
     Your variable names might be different! Yes, this will be a long line 
     of code that will likely wrap onto the next couple of lines (that's 
     okay). 

    11. Let's read our Mad Libs story! Click Run, when your program 
    runs follow the prompts and enter the input requested. Copy the 
    output and paste on line one of your code as a multi line comment 

    '''

    #DON"T EDIT THE CODE BELOW This is The template for the story 
    STORY = """This morning I woke up and felt %s because _ was going to finally %s over the big _ %s. On the other side of the %s were many %s protesting to keep %s in stores. The crowd began to _ to the rhythm of the %s, which made all of the %s very _. %s tried to _ into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping _ into a puddle of %s. %s then fell asleep and woke up in the year _, in a world where %s ruled the world."""


    #YOUR CODE HERE