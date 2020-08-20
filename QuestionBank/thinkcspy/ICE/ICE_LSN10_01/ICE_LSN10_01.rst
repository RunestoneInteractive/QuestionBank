.. activecode:: ICE_LSN10_01
    :author: jenkins
    :difficulty: 3.0
    :basecourse: thinkcspy
    :chapter: ICE
    :subchapter: ICE_LSN10_01
    :topics: ICE/ICE_LSN10_01
    :from_source: F
    :nocanvas:

    ### Function to change Celsius to Fahrenheit.
    def ctof(c):
     return 9/5 * c + 32

    ### Function to change Fahrenheit to Celsius.
    def ftoc(f):
     return 5/9 * f - 32

    #Change 0C to F
    tempC = 0
    FTemp = ctof(tempC)
    print("tempC = 0 changed to FTemp = " + str(FTemp))

    #Change 32F to C
    tempF = 32
    CTemp = ftoc(tempF)
    print ("tempF = 32 changed to CTemp = " + str(CTemp))