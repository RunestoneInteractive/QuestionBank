.. mchoice:: peerwiseqb_4052675
    :basecourse: peerwiseqb
    .. role:: raw-html-m2r(raw)    
       :format: html    
        
        
    **2014_Q15:**    
        
    Consider the array called values initialised as follows:    
        
    int values[5] = {1,2,3,4,5};    
        
    What would be stored in the elements of this array after the following code    
    has executed?    
        
    int i = 0;\ :raw-html-m2r:`<br>`    
    while (i < 5) {\ :raw-html-m2r:`<br>`    
       values[(i+1)%5] = values[i];\ :raw-html-m2r:`<br>`    
       i++;\ :raw-html-m2r:`<br>`    
    }    
    

    - { 1, 1, 1, 1, 1 }    
      

      + Correct!
    - { 5, 1, 2, 3, 4 }    
      

      - Incorrect
    - { 2, 3, 4, 5, 2 }    
      

      - Incorrect
    - { 2, 3, 4, 5, 1 }    
      

      - Incorrect
    - { 1, 1, 2, 3, 4 }    
      

      - Incorrect
